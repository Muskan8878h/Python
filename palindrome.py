a=input()         #a=[ : : -1]
def fun(a):
    b=a.replace(' ','').lower()
    return b==b[: :-1]
result=fun(a)
if result:
    print(a,"palindrome")
else:
    print("not a palindrome")
