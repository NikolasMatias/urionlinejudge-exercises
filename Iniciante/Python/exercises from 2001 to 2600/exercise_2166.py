repeticoes = int(input())
raiz2 = 1
fracao = 1/2
if repeticoes == 0:
    print('{:.10f}'.format(raiz2))
else:
    for x in range(repeticoes-1):
        fracao = 1 / (2+fracao)
    print('{:.10f}'.format(raiz2 + fracao))