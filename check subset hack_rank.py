t=int(input())
for _ in range(t):
    ln_a=int(input())
    set_a=set(map(int,input().split()))
    ln_b=int(input())
    set_b=set(map(int,input().split()))
    print(len(set_b.intersection(set_a)) == ln_a)
