def doesntHaveTwoValidGrades(grades):
    if isinstance(grades, list) and len(grades):
        count_valid_grades = 0
        for analised_grade in grades:
            if 0 <= analised_grade <= 10:
                count_valid_grades += 1

        if count_valid_grades >= 2:
            return False
    return True

def repeatGradeCalculation():
    print('novo calculo (1-sim 2-nao)')
    confirm = int(input())
    while confirm not in [1,2]:
        print('novo calculo (1-sim 2-nao)')
        confirm = int(input())

    if confirm == 1:
        executeGradeCalculation()

def executeGradeCalculation():
    grades = []

    while len(grades) == 0 or doesntHaveTwoValidGrades(grades):
        grades.append(float(input()))

    for grade in grades:
        if not 0 <= grade <= 10:
            print('nota invalida')

    filtered_grades = []
    for analised_grade in grades:
        if 0 <= analised_grade <= 10:
            filtered_grades.append(analised_grade)

    print(''.join([
        'media = ',
        '{:.2f}'.format(sum(filtered_grades)/len(filtered_grades))
    ]))

    repeatGradeCalculation()

executeGradeCalculation()