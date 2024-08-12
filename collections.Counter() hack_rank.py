no_of_shoes = int(input())
size_lst = map(int,input().split(' '))
no_of_customers = int(input())

from collections import counter
shoes = counter(size_lst)

income = 0
for i in range(no_of_customers):
    size , price = map(int,input().split(' '))
    if shoes[size]:
        income +=price
        shoes[size] -=1
print(income)