count = int(input())
valores = [int(x) for x in input().split()]
valores = valores[(-1)*count::]
multiplos = [2,3,4,5]
for valor in multiplos:
    multiplo = [1 for x in valores if x%valor == 0].count(1)
    print(''.join([str(multiplo), ' Multiplo(s) de ', str(valor)]))
