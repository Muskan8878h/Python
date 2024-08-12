main=set(input().split())
n=int(input())
total =set()
for _ in range(n):
    total = total.union(set(input().split()))
print(len(total) == len(main.intersection(total)))