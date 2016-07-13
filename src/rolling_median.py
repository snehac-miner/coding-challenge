__author__ = 'snehachalla'
#date:  7/11/2016

'''
Use matrices
O(n*n) to loop through the half triangular matrix to check for 60 sec window using timestamp stored here.
Use dictionary to store row names
Use hash map/dict to store degrees
#Use adjacency list instead of matrices
'''

import json
import numpy
from datetime import datetime
import sys
import getopt

input_file = sys.argv[1]
output_file = sys.argv[2]


'''
Vertex class stores the Venmo user's username as id. It stores the user's payees and the time stamp of payment in a
dictionary by name connectedTo. Essentially connectedTo{} is a adjacency list for each user.
Using adjacency lists instead of a single list for all users reduces the time complexity because you don't have to iterate to
every user to be able to access the elements of a single user.
Also since every Venmo user is not connected to every other user, using adjacency lists instead of adjacency matrix saves space.
'''
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    #addNeighbor method adds the new vertex and stores the timestamp as soon as the current user gets paid.
    def addneighbour(self,nbr,timestamp):
        self.connectedTo[nbr] = timestamp

    # This method returns the string list of neighbors the current user is connected to
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    #getconnections method returns the list of names of all users that the current user paid in the last 60 sec time window
    def getconnections(self):
        return self.connectedTo.keys()

    #getid method return the id or name of the current user
    def getid(self):
        return self.id

    #timestamp returns the time of payment between current user and a neightbour with name nbr
    def timestamp(self,neibr):
        return self.connectedTo[neibr]

    #getdegree method returns the number of users the current user is connected to
    def getdegree(self):
        return len(self.connectedTo.keys())

    #delNeighbour method deletes a user from the list of users which the current user paid to
    def delNeighbour(self, name):
        del self.connectedTo[name]


'''
Graph class maintains the list of vertices and the maximum timestamp.
It also provides methods to manipulate the graph
'''
class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.current_maxtimestamp = None

    # addVertex method add a vertex to a graph and increments the number of vertices.
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    #addEdge method adds an edge between user 'f' and user 't' after f pays t at a particular timestamp within the 60 sec window
    def addEdge(self,f,t,timestamp):
        if self.numVertices == 0:
            self.current_maxtimestamp = timestamp

        if (self.checkWindowTimeGreaterThan60(timestamp)==False):
            if f not in self.vertList:
                nv = self.addVertex(f)
                self.vertList[f] = nv
            if t not in self.vertList:
                nv = self.addVertex(t)
                self.vertList[t] = nv
            self.vertList[f].addneighbour(self.vertList[t].getid(), timestamp)
            self.vertList[t].addneighbour(self.vertList[f].getid(), timestamp)

    '''
    flushgraph method removes the edges which do not fall in the 60seconds timespan window by iterating through the vertices
    in the graph
    It also deletes the vertices with degree zero after flushing out the edges which are out of the 60sec window from
    current maxtimestamp
    '''
    def flushgraph(self,timestamp):

        neighbours_del = [] #This list stores the key,value pairs to be deleted
        for key in self.vertList :
             vertex_obj= self.vertList[key]

             for nbrs in vertex_obj.getconnections() :
                 if self.checkWindowTimeGreaterThan60(vertex_obj.connectedTo[nbrs]):
                     neighbours_del.append((key,nbrs))

        for (k,v) in neighbours_del:
                  ver_obj= self.vertList[k]
                  ver_obj.delNeighbour(v)
        for v in self.vertList.keys():
             if self.vertList[v].getdegree() ==0:
                       del self.vertList[v]

      #getVertex method returns the vertex object of a user with name 'n'
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    #This methods lists the list of all names of the users/vertex ids in the graph
    def __contains__(self,n):
        return n in self.vertList

    #This method prints the names of all users in the current graph.
    def getVertices(self):
        return self.vertList.keys()


    def __iter__(self):
        return iter(self.vertList.values())

    #median_degree returns the median degree of the users in the current graph
    def median_degree(self):
        li = []
        for key in self.vertList:
            li.append(self.vertList[key].getdegree())
        return numpy.round( numpy.median( numpy.around(numpy.array(li),2)), decimals=3)

    #Deletes a vertex in the graph/ removes a user from the graph
    def deleteVertex(self,v):
             del self.vertList[v]

    #Returns True if the time gap between the new user transaction and current max timestamp is greater than 60 seconds.
    # Returns false otherwise
    def checkWindowTimeGreaterThan60(self,timestmp1):

            if self.current_maxtimestamp >= timestmp1:
                diff = self.current_maxtimestamp-timestmp1
            else:
                diff = timestmp1-self.current_maxtimestamp

            a = str(diff).split(',')
            # len(a) >1 one time difference is greater than 1 day or 24 hours.
            if (len(a)>1):
                return True
            else:
                d = a[0]
                e = d.split(':')
                  #e is a array of length 3 which contains hours, minutes and seconds
                  #e[0] is hours ,e[1] is minutes and e[2] is seconds
                if (int(e[1])> 0 or int(e[0])>0 ):
                    return True
                else:
                    return False

'''
Invoking the readandadd method of transactions class begins the reading the input file and
outputs the resulting rolling medians to output.txt file
'''

class Transactions(object):
    def readandadd(self, input_path, output_path):
        rolling_median =  []
        #path = raw_input("Enter the relative path of the coding challenge folder in a new line \n")
        f = open(input_path, 'r')
        venmo_graph = Graph()
        for l1 in f:
            if l1 != '\n':    # Read until the last line before the start of the blank lines.
                li = l1.split(',') #splits the three different fields
                actor = li[-1].split(':') #last element in order is the actor
                keys = actor[-1][2:-3] #store the name of the actor by stripping \" and \}
                key = keys.strip() #strip all white spaces in the ends
                created_time = li[0].strip().split('e":') #first field in each line is created_time
                times =   created_time[-1][2:-2] #remove the ending characters and Z
                time = times.strip()
                time1 = list(time)
                time1[10]=' ' #blank T
                time2 = "".join(time1)
                date_object = datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')  #convert the string to a datetime object
                targets = li[1].split(':') #get the target user name
                target = targets[1][2:-1]
                target = target.strip() #strip it off white spaces

                #If it is the first vertex in the graph set the maxtimestamp of the graph to current date object
                if venmo_graph.numVertices==0 :
                    venmo_graph.current_maxtimestamp = date_object

                #If the timestamp of the incoming transaction falls within 60 secs of Graph current_maxtimestamp then
                #flush the edges and add the edge
                if (venmo_graph.checkWindowTimeGreaterThan60(date_object)==False):
                    if venmo_graph.current_maxtimestamp < date_object:
                         venmo_graph.current_maxtimestamp = date_object
                         venmo_graph.flushgraph(date_object)

                    venmo_graph.addEdge(key,target,date_object)
                    rolling_median.append(venmo_graph.median_degree())
                # If incoming timestamp is out of 60 secs window them ignore the input and retain the same graph
                if (venmo_graph.checkWindowTimeGreaterThan60(date_object)):
                    rolling_median.append(rolling_median[-1])

                # Send the current rolling medians to the output.txt file.
                f1 = open(output_path , 'w' )
                for i in rolling_median:
                    print >>f1, numpy.round(i,3)
                f1.close()


start_transactions = Transactions()
start_transactions.readandadd(input_file, output_file)


































