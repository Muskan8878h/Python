list_1=[8,3,2,4,9,1]
def rotate_list(list_1,n):
    for i in range(n):
        list_1.insert(0,list_1.pop())
    return list_1
rotated_list=rotate_list(list_1,3)
print(rotated_list)
