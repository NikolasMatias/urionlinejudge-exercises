def get_fibonacci(number):
    fibonacci_number = [0, 1]
    if number <= 0:
        return 0
    if number <= 1:
        return 1
    else:
        for x in range(2, number+1):
            fibonacci_number.append(fibonacci_number[x-1] + fibonacci_number[x-2])
        return fibonacci_number[-1]



countLoop = int(input())
valores = []

for x in range(countLoop):
    number = int(input())
    valores.append([number, get_fibonacci(number)])

for valor in valores:
    number, fibonacci = valor
    print(''.join(['Fib(', str(number), ') = ', str(fibonacci)]))