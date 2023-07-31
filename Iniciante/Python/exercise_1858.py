quantidade_n = int(input())
valores = [int(x) for x in input().split()]
resposta_certa = 0
repete = False
valor_repete = 0
for x in range(1, quantidade_n):
    if valores[x] < valores[x-1]:
        resposta_certa = x+1
    elif valores[x] == valores[x-1]:
        repete = True
        valor_repete = valores[x]
        resposta_certa = x
for x in range(1, quantidade_n):
    if valor_repete == valores[x]:
        resposta_certa = x+1
        break
print(str(resposta_certa))