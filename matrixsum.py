a=[[1,2,3],[3,4,5]]
b=[[4,5,6],[7,8,9]]
def matrix_addition(a,b):
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
        raise valueError("Matrix must have the same dimensions for addition")
    num_rows=len(a)
    num_cols=len(a[0])
    result_matrix=[[0,0,0],[0,0,0]]
    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[i][j]=a[i][j]+b[i][j]
    return result_matrix
result_matrix=matrix_addition(a,b)
for row in result_matrix:
    print(row)