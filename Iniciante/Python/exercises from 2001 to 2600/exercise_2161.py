repeticoes = int(input())
raiz10 = 3
fracao = 1/6
if repeticoes == 0:
    print('{:.10f}'.format(raiz10))
else:
    for x in range(repeticoes-1):
        fracao = 1 / (6+fracao)
    print('{:.10f}'.format(raiz10 + fracao))