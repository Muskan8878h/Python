n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    for k in range(i):
        print("  ",end="")
    for j in range(n-i):
        print("*",end="")

    print()

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    for j in range(n-i-1):
        print("  ",end="")
    for k in range(i+1):
        print("*",end="")
    print()

S