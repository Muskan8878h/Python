student=[]
for i in range(int(input())):
    name=input()
    score=int(input())
    student.append([name,score])
print(student)

student_score=[i[1] for i in student]
print(student_score)

student_score.sort()
sorted_score=set(student_score)
print(sorted_score)


