n=int(input())
i=1
while i<=n:
    j=1
    k=n
    while j<=n:
        print(k,end='')
        j+=1
        k-=1
    print()
    i+=1


n=int(input())
for i in range(n):
    k=n
    for j in range(n):
        print(k,end="")
        k-=1
    print()