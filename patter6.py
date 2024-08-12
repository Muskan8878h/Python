n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end='')
    print()


i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j+=1
    print()
    i+=1