if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
    find_score=[x[1] for x in student]
    set_score=sorted(set(find_score))
    find_name=sorted([y[0] for y in student if (set_score[1]==y[1])])
    for z in find_name:
        print(z)
