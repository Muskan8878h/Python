#1
#1 2
#1 2 3
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end='')
    print()

#3 3 3
#3 3
#3
for i in range(n):
    for j in range(n-i):
       print(n,end='')
    print()

#1 1 1 1
#2 2 2
#3 3
#4
k=0
for i in range(n):
    k+=1
    for j in range(n-i):
        print(k,end='')
    print()

#1
#2 2
#3 3 3
k=0
for i in range(n):
    k+=1
    for j in range(i+1):
        print(k,end="")
    print()

#3 3 3
#2 2
#1
k=n+1
for i in range(n):
    k-=1
    for j in range(n-i):
        print(k,end='')
    print()



