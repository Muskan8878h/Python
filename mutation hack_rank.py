def mutate_string(string, position, character):
    my_string=list(string)
    my_string[position]=character
    my_final_string="".join(my_string)
    return(my_final_string)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)