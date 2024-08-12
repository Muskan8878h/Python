b=[]
n=int(input())
m=int(input())
for i in range(n):
    a=[]
    for j in range(m):
        v=int(input())
        a.append(v)
    b.append(a)
#print(b)

count1=0
for i in range(n):
    for j in range(m):
        #print(b[i][j])
        p=b[i][j]
        count=0
        for k in range(1,p+1):
            if p%k==0:
                count+=1
        if count!=2:
            count1+=1

print("output is ",count1)

