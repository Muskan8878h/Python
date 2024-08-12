n=int(input())
n1=len(str(n))
sum=0
n2=n
while n>0:
    dig=n%10
    sum+=dig**n1
    n=n//10
if sum==n2:
    print("armstrong no.")
else:
    print("not armstrong")
