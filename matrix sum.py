def sum_row(matrix):
    for i,row in enumerate(matrix):
        row_sum=sum(row)
        print(f"sum of row {i+1}={row_sum}")
matrix=[
        [2,1,3,4],
        [5,2,9,5],
        [8,3,10,48]
        ]
sum_row(matrix)
