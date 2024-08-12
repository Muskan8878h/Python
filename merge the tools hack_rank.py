def merge_the_tools(string, k):
    start = 0
    end = k
    while end <= len(string):
        temp = string[start:end]
        result = ''.join(sorted(set(temp), key=temp.index))
        print(result)
        start += k
        end += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)