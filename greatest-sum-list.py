n=int(input())
li=[]
v1=0
v2=0
for i in range(0,n):
    v=int(input())
    li.append(v)
maxsum=0
sum=0
for i in range (0,n-1):
    for j in range (i+1,n):
        sum=li[i]+li[j]
        if sum>maxsum:
            maxsum=sum
            v1=li[i]
            v2=li[j]
print(v1,v2)
s=v1+v2
print(s)
