def sum(n):                        #recursion
    if n<=10:
        return n
    else:
        return n%10+sum(n//10)
print(sum(12345))




a=int(input())                                    #GCD greatest common divisor
b=int(input())
def gcd(a,b):
    if  b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(a,b))