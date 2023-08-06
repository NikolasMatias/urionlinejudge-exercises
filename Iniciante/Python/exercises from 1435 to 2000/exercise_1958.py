number = float(input())
print('+' if '-' not in str(number) else '', end='')
print('{:.4e}'.format(number).upper())