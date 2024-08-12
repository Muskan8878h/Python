# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N=int(input())
    lst=map(int, input().split())
    lst_tuple=tuple(lst)

    print(hash(lst_tuple))

