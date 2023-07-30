def hasNotZeroValue(numbers):
    if isinstance(numbers, list) and len(numbers) > 0:
        for number in numbers:
            if number == 0:
                return False
        return True
    return True

def findQuadrantFromCoordinates(valorX, valorY):
    if valorX > 0 and valorY > 0:
        return 'primeiro'
    elif valorX < 0 and valorY > 0:
        return 'segundo'
    elif valorX < 0 and valorY < 0:
        return 'terceiro'
    else:
        return 'quarto'

listResults = []

while len(listResults) == 0 or hasNotZeroValue(listResults[-1]):
    valorA, valorB = [int(x) for x in input().split()]
    listResults.append([valorA, valorB])

listResults.pop()

for result in listResults:
    valorX, valorY = result
    print(findQuadrantFromCoordinates(valorX, valorY))