# Read number of students and subjects
n, x = map(int, input().split())

# Read subject-wise marks
marks = []
for _ in range(x):
    marks.append(list(map(float, input().split())))

# Calculate and print averages student-wise
for student_marks in zip(*marks):
    avg = sum(student_marks) / x
    print(avg)
