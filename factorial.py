n=int(input())
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    return fact
a=fact(n)
print(a)



def factorial(x):
    if x==1 or x==0:
        return 1
    else:
        return x*factorial(x-1)
x=int(input())
print("factorial is :",factorial(x))