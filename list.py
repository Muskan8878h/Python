def creat_list(r1,r2):
    return list(range(r1,r2+1))
r1=-1
r2=1
print(creat_list(r1,r2))

import itertools
r1=5
r2=20
n=list(itertools.chain(range(r1,r2)))
print(n)

a=[10,20,30,40,50,60]
a.append(80)
a.insert(2,"hello")
print(a)

a=[1,9,3,4]
b=[5,7,7,2]
a.extend(b)
print(a)
print(sum(a))
print(a.count(7))   #repeated values count
print(a.index(7))   #position of element
print(min(a))
print(max(a))
a.sort()            #sort a list
print(a)
a.pop(1)            #to remove a digit from his index position
print(a)
del a[3]            #to remove a digit from his index position
print(a)
a.remove(1)         #to remove a digit which we initialise in list
print(a)





