students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(list(set([student[1] for student in students])))
second_lowest = scores[1]

second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest])

for student in second_lowest_students:
    print(student)
