while True:
    valores = [int(x) for x in input().split()]
    if len(valores) == 1 and valores[0] == 0:
        break
    valor_a, valor_b, valor_c = valores
    area_casa = valor_a*valor_b
    area_ideal = int(area_casa*100/valor_c)
    print(str(int(area_ideal**(1/2))))
