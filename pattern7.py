n=int(input())
for i in range(n):
    for j in range(n):
        print(j+1,end='')
    print()



n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print(j,end='')
        j+=1
    print()
    i+=1