n=int(input())
n1=set(map(int,input().split()))
m=int(input())
m1=set(map(int,input().split()))
a=n1.symmetric_difference(m1)
count=0
for i in a:
    count+=1
print(count)