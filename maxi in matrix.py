def maximum(a):
    if not a:
        return None
    m=a[0][0]
    for row in a:
        for i in row:
            if i>m:
                m=i
    return m
a=[
    [1,2,3,4],
    [5,6,7,8],
    [1,4,7,2]
    ]
m=maximum(a)
print(m)
