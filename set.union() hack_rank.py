n=int(input())
n1=set(map(int,input().split()))
m=int(input())
m1=set(map(int,input().split()))
res = n1.union(m1)
count=0
for i in res:
    count+=1
print(count)