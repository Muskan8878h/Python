n=int(input())
s=1
while n>0:
    s=s*(n%10)
    n=n//10
print(s)