number = int(input())
numbers = []

for x in range(number):
    numbers.append(int(input()))

for newNumber in numbers:
    if newNumber == 0:
        print('NULL')
    else:
        if newNumber % 2 == 0:
            if newNumber > 0:
                print('EVEN POSITIVE')
            elif newNumber < 0:
                print('EVEN NEGATIVE')
        else:
            if newNumber > 0:
                print('ODD POSITIVE')
            elif newNumber < 0:
                print('ODD NEGATIVE')