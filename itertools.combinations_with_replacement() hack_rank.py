from itertools import combinations_with_replacement
s,k = input().split()
k = int(k)
for i in list(combinations_with_replacement(sorted(s),k)):
    print(''.join(i))