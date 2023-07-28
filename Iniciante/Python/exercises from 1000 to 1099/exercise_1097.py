numbersLoop = list(range(1, 10, 2))
valorJ1 = 7
valorJ2 = 6
valorJ3 = 5

for i in numbersLoop:
    print(''.join(['I=', str(i), ' J=', str(valorJ1)]))
    print(''.join(['I=', str(i), ' J=', str(valorJ2)]))
    print(''.join(['I=', str(i), ' J=', str(valorJ3)]))
    valorJ1 += 2
    valorJ2 += 2
    valorJ3 += 2