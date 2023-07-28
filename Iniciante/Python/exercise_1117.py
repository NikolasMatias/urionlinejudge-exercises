def isValidGrade(grade):
    return 0 <= grade <= 10

def getListValidGrades(grades):
    return list(filter(lambda analised_grade: isValidGrade(analised_grade), grades))


def doesntHaveTwoValidGrades(grades):
    if isinstance(grades, list) and len(grades):
        filtered_grades = getListValidGrades(grades)
        if len(filtered_grades) >= 2:
            return False
    return True

def avgGrades(grades):
    if isinstance(grades, list) and len(grades) > 0:
        return sum(grades)/len(grades)
    return 0.0

grades = []

while len(grades) == 0 or doesntHaveTwoValidGrades(grades):
    grades.append(float(input()))

for grade in grades:
    if not isValidGrade(grade):
        print('nota invalida')

filteredGrades = getListValidGrades(grades)

print(''.join([
    'media = ',
    '{:.2f}'.format(avgGrades(filteredGrades))
]))
