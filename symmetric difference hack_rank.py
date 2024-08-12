a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
x=set(b)
y=set(d)
p=y.difference(x)
q=x.difference(y)
r=p.union(q)
print("\n".join(sorted(r,key=int)))


#OR


a = int(input())
set_a = set(input().split())
c = int(input())
set_c = set(input().split())
result_set = set_a.symmetric_difference(set_c)
print("\n".join(sorted(result_set, key=int)))
