n = int(input())

array = []
for i in range(n):
    a,b = input().split()
    array.append((a, b))

array.sort(key=lambda student: student[1])

for student in array:
    print(student[0], end = ' ')