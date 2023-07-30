valor_a, valor_b = [int(x) for x in input().split()]
resto = valor_a%abs(valor_b)
quociente = int((valor_a-resto)/valor_b)
print(' '.join([str(quociente), str(resto)]))