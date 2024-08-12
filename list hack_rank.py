if __name__ == '__main__':
    N=int(input())
    List=[]
    for i in range(N):
        user_input=input().split()
        if user_input[0]=="insert":
            List.insert(int(user_input[1]), int(user_input[2]))
        elif user_input[0]=="print":
            print(List)
        elif user_input[0]=="remove":
            List.remove(int(user_input[1]))
        elif user_input[0]=="append":
            List.append(int(user_input[1]))
        elif user_input[0]=="sort":
            List.sort()
        elif user_input[0]=="pop":
            List.pop()
        elif user_input[0]=="reverse":
            List.reverse()
