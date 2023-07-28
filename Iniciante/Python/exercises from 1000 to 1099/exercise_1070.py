number = int(input())
lastNumber = 11

if number%2 == 0:
    number += 1

for x in range(number, (number+lastNumber), 2):
    print(x)