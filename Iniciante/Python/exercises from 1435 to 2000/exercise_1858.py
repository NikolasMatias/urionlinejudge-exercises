quantidade_n = int(input())
valores = [int(x) for x in input().split()]
resposta_certa = 0
minValue = min(valores)

for x in range(quantidade_n):
    if valores[x] == minValue:
        resposta_certa = x+1
        break

print(str(resposta_certa))