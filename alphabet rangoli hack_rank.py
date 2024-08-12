def print_rangoli(size):
    # your code goes here
    alphabet = [chr(i) for i in range(97,123)]
    alphabet = alphabet[:size]
    indices = list(range(size))
    indices = indices[:-1] + indices[::-1]
    for i in indices:
        start_index = i+1
        original = alphabet[-start_index:]
        reverse = original[::-1]
        row = reverse+original[1:]
        width = size*4-3
        row = '-'.join(row).center(width, "-")
        print(row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)