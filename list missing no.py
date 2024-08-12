list_1=[1,2,3,4,5,6,7,8,9,10]
list_2=[3,5,10,9]
def missing(list_1,list_2):
    list_3=[ ]
    for i in list_1:
        if i in list_1 and i not in list_2:
            list_3.append(i)
    return list_3
print(missing(list_1,list_2))