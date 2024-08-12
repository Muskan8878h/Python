l1=[8,3,2,4,9,1]               #print (l1 or l2)
l2=[7,4,8,3,1,9,10]
def common(l1,l2):
    l3=[ ]
    for i in l1:
        if i in l2 and i not in l3:
            l3.append(i)
    return l3
c=common(l1,l2)
print(c)
