def rotate_list(lst,n):
    return lst[-n:]+lst[:-n]
original_list=[1,2,3,4,5]
rotation_count=2
rotated_list=rotate_list(original_list,rotation_count)
print("original list:",original_list)
print("Rotated list:",rotated_list)
