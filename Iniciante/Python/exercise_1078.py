number = int(input())

for x in range(1, 11):
    print(''.join([str(x), ' x ', str(number), ' = ', str(number*x)]))