num_students = int(input())
students = {}
for x in range(num_students):
    code, grade = input().split()
    grade = float(grade)
    students[code] = grade
is_minimum_reached = [1 for grade in students.values() if grade >= 8].count(1)
if is_minimum_reached:
    highest_grade = ''
    for code in students.keys():
        if len(highest_grade) > 0:
            if students[code] > students[highest_grade]:
                highest_grade = code
        else:
            highest_grade = code
    print(highest_grade)
else:
    print('Minimum note not reached')