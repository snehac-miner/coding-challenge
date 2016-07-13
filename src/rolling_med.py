__author__ = 'snehachalla'

import json
import numpy
from datetime import datetime

f = open('/Users/snehachalla/Documents/Data Science/coding-challenge/venmo_input/venmo-trans.txt', 'r')

def compute_median_degree(payments):
    degree_of_nodes = {}
    #print payments
    for (a,b,c) in payments:
        if a in degree_of_nodes.keys():
                degree_of_nodes[a]= degree_of_nodes[a] + 1
        else:  degree_of_nodes[a] = 1
        if b in degree_of_nodes.keys():
                degree_of_nodes[b]= degree_of_nodes[b] + 1
        else:
               degree_of_nodes[b] = 1
    ordered_values =  degree_of_nodes.values()
    ordered_values = sorted(ordered_values)
    #print  numpy.median(ordered_values)
    #print ordered_values
    return numpy.median(ordered_values)

dict = {}
payments_li = []
medians_trace = []
max_timestamp = None
#print l1
for l1 in f:
  if l1 != '\n':    # Read until the last line before the start of the blank lines.
    li_remove = []
    li = l1.split(',')
    actor = li[-1].split(':')
    keys = actor[-1][2:-3]
    key = keys.strip()
    created_time = li[0].strip().split('e":')
    times =   created_time[-1][2:-2]
    time = times.strip()
    time1 = list(time)
    time1[10]=' '
    time2 = "".join(time1)
    date_object = datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
    targets = li[1].split(':')
    target = targets[1][2:-1]
    target = target.strip()
    #print key, target,date_object

    #If it is the first payments add it to the list
    if len(payments_li)== 0:
            payments_li.append((key, target,date_object))
            max_timestamp =  date_object
    else:
        if date_object >=max_timestamp : max_timestamp = date_object
        indexes =[]
        payments_li.append((key,target,date_object))
        for i in range(0,len(payments_li)-1):
            (a,b,c)= payments_li[i]
            if ((a,b)==(key,target)) or ((a,b) == (target,key)) :
                indexes.append(i)
        for i in range(0,len(payments_li)):
             (a,b,c)= payments_li[i]
             diff = max_timestamp-c
             a = str(diff).split(',')
             if (len(a)>1):
                indexes.append(i)
             else:

                  d = a[0]
                  e = d.split(':')
                  #print e[0],e[1]
                  if (int(e[1])> 0 or int(e[0])>0 ):
                      indexes.append(i)
        indexes = set(indexes)
        #print indexes
        for i in indexes:
            li_remove.append(payments_li[i])
        if len(li_remove)!=0:
            payments_li = [(d,e,f) for (d,e,f) in payments_li if (d,e,f) not in li_remove]
    print payments_li
    medians_trace.append(compute_median_degree(payments_li))
    f1 = open('/Users/snehachalla/Documents/Data Science/coding-challenge/venmo_output/output.txt' , 'w' )
    for i in medians_trace:
         print >> f1 , i
    f1.close()












































'''

    if key  in dict.keys():   pass
    else:
          dict[key] = []
          dict[key].append((target, time))

    if key in dict.keys():
      li  = dict[key]
      i =0
      for (a,b) in li:
        i = i+1
        if a == target :
            del li[i-1]
      dict[key].append((target, time))
f.close()

for i in dict.keys():
    print i,dict[i]
'''
'''
def dosomething(txt):
       list = txt.split(',')
       actor = list[2].split(':')
       key = actor[1][2:-3]
       created_time = list[0].split('":')
       time =   created_time[1] [2:-1]
       target = list[1].split(':')
       target = target[1][2:-1]
       return key, time,target

dict = {}
with open('/Users/snehachalla/Documents/Data Science/coding-challenge/venmo_input/venmo-trans.txt') as openfileobject:
    for line in openfileobject:
       key, time,target =  dosomething(line)
       print key,time,target
       if dict.has_key(key): {}
       else:
          dict[key] = []
          dict[key].append((target, time))

       if dict.has_key(key):
          li  = dict[key]
          i =0
          for (a,b) in li:
            i = i+1
            if a == target :
                del li[i-1]
          dict[key].append((target, time))
print dict
openfileobject.close()

'''









