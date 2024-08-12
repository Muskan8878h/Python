n=int(input())
for i in range(n):
    for j in range(i+1):
        print(1,end="")
    print()


i=1
while i<=n:
    j=1
    while j<=i:
        print(1,end="")
        j+=1
    print()
    i+=1