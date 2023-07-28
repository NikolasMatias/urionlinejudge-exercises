number = int(input())

for x in range(1, number):
    if x%2 == 0:
        print(''.join([str(x), '^2 = ', str(x**2)]))

if number%2 == 0:
    print(''.join([str(number), '^2 = ', str(number**2)]))