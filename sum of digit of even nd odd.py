n=int(input())
even=0
odd=0
while n>0:
    remainder=n%10
    if n%2==0:
        even=even+remainder
    else:
        odd=odd+remainder
    n=n//10
print(even,'  ',odd)O