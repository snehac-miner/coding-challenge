__author__ = 'snehachalla'
'''
from datetime import datetime
li = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]

for (a,b,c) in li:
    if a ==1 and b==2 :
        print 'yes'


date_object1 = datetime.strptime('2016-04-07 03:31:18', '%Y-%m-%d %H:%M:%S')
date_object2 = datetime.strptime('2016-04-07 03:31:59', '%Y-%m-%d %H:%M:%S')
diff = date_object2-date_object1
print diff
a = str(diff).split(',')
print a
'''

dict = { 'arthur':1 , 'butcher':2 , 'catherine':3 }
'''
k = dict.values()
print k
print type(k)
print sorted(k)
import numpy
print numpy.median(sorted(k))

f1 = open('/Users/snehachalla/Documents/Data Science/coding-challenge/venmo_output/output.txt' , 'w' )
for i in k:
    print >> f1 , i
f1.close()
'''

if 'arthur' in dict.keys():
    dict['arthur'] = dict['arthur']+ 1
#print dict
'''
from datetime import datetime
date_object1 = datetime.strptime('2016-04-07 03:34:58', '%Y-%m-%d %H:%M:%S')
date_object2 = datetime.strptime('2016-04-07 03:33:19', '%Y-%m-%d %H:%M:%S')

#print date_object2>=date_object1

print date_object1-date_object2





li = [3,2,2,4,5,6,6]
#li=set(li)

for i in li:
    print i

lir = [3,4]

li = [value for value in li if value not in lir]

print li

print li[:-1]
'''

'''
s = set([])

s.add(1)
s.add(2)
s.add(3)

s.add(3)

print s

'''
'''
dict = {1: 'apple',2:'orange' }

print 'apple' in dict

print len(dict.keys())

del dict[1]


print dict
'''
import json
with open('/Users/snehachalla/Documents/Data Science/coding-challenge/venmo_input/venmo-trans.txt', mode='r') as f:
    python_data = json.load(f)
print((python_data))














