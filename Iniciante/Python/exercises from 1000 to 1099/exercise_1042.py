numbers = [int(x) for x in input().split()]
sortedNumbers = numbers.copy()
sortedNumbers.sort()

for number in sortedNumbers:
    print(str(number))

print('')

for number in numbers:
    print(str(number))