num_abas, num_acoes = [int(x) for x in input().split()]
for x in range(num_acoes):
    acao = input()
    if acao == 'fechou' and num_abas > 0:
        num_abas += 1
    elif acao == 'clicou':
        num_abas -= 1
print(str(num_abas))