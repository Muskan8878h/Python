n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print('*',end='')
        j+=1
    print()
    i+=1

i=n-1
while i>0:
    j=1
    while j<=i:
        print('*',end='')
        j+=1
    print()
    i-=1