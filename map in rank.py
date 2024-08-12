n = int(input())
arr = map(int, input().split())
res=sorted(set(arr))[-2]
print(res)