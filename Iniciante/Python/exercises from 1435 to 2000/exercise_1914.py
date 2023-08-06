countLoops = int(input())
for x in range(countLoops):
    nome_1, opcao_1, nome_2, opcao_2 = [str(y) for y in input().split()]
    valor_1, valor_2 = [int(y) for y in input().split()]
    soma = valor_1+valor_2
    if soma%2 == 0:
        print(nome_1 if opcao_1 == 'PAR' else nome_2)
    else:
        print(nome_1 if opcao_1 == 'IMPAR' else nome_2)