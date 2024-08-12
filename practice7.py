n=int(input())
def fab(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        return fab(n-1)+fab(n-2)
result=fab(n)
print(result)
