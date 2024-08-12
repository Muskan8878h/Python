set1={1,2,3,4,5}
set1.add(10)
print("add",set1)

set1.update([1,5,8])
print("update",set1)

set1.remove(3)
print("remove",set1)

set1.pop()
print("pop",set1)

set2={3,4,5,6,7}
print("difference",set2-set1)

l1=[1,2,3,4,5,5]
x=set(l1)
print("chnage in list",x)
y=list(x)
print("chnage in set",y)


set1.intersection(set2)
print("intersection",set1)

a={1,2,2,3}
b={4,5,6,87,9,6}
c=a.issubset(b)
print("subset",c)

d=a.issuperset(b)
print("superset",d)

set1={1,2,3}
set1=[x**2 for x in set1]
print("square",set1)






