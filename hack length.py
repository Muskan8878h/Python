sample_str = input()
K = int(input())

# Getting Kth element of each word
result = ''.join(sub[K] for sub in sample_str.split())

# Printing result
print(result)
