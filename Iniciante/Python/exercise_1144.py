valorN = int(input())
count = 0
numberBase = 1

for x in range(valorN*2):
    values = []
    if count == 0:
        values = [
            numberBase,
            numberBase**2,
            numberBase**3
        ]
        count = 1
    elif count == 1:
        values = [
            numberBase,
            (numberBase ** 2)+1,
            (numberBase ** 3)+1
        ]
        count = 0
        numberBase += 1
    print(' '.join(str(y) for y in values))