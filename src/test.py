__author__ = 'snehachalla'



list = '{"created_time": "2016-04-07T03:35:02Z", "target": "Connor-Liebman", "actor": "Nick-Shirreffs"}'.split(',')

print list[0] , list[1] , list[2]

actor = list[2].split(':')
key = actor[1][2:-2]
print key
created_time = list[0].split('e":')
time =   created_time[1] [2:-1]
print time
target = list[1].split(':')
target = target[1][2:-1]
print target

dict = {}

if key not in dict.keys():
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

