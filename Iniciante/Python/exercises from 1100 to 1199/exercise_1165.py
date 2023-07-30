def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

countLoop = int(input())
valores = []

for x in range(countLoop):
    number = int(input())
    if is_prime(number):
        valores.append(''.join([str(number), ' eh primo']))
    else:
        valores.append(''.join([str(number), ' nao eh primo']))

for valor in valores:
    print(valor)