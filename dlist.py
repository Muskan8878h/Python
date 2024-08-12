b=[]
m=int(input("row"))
n=int(input("col"))
for i in range(m):
    a=[]
    for j in range (n):
        v=int(input())
        a.append(v)
    b.append(a)
print(b)