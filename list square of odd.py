list1=[1,8,3,2,4,5,7]
list2=[ ]
for i in list1:
    if i%2!=0:
        list2.append(i**2)
print(list2)