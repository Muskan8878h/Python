n=int(input())
s=0
org=n
a=1
while n>=a:
    s=s+(n%10)*(n%10)*(n%10)
    n=n//10
if(org==s):
    print("Armstrong")
else:
    print("Not an Armstrong")