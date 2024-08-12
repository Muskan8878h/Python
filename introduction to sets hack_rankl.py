def average(array):
    # your code goes here
    sum_arr = sum(set(arr))
    len_arr = len(set(arr))
    avg = sum_arr/len_arr
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)