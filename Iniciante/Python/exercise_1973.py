# n = int(input())
# x = [int(x) for x in input().split()]
# total = sum(x)
# atacadas = [0]*n
# i = 0
# while 0 <= i < n:
#     lado = x[i]%2
#     if x[i] > 0:
#         x[i] -= 1
#         atacadas[i] = 1
#         total -= 1
#     if lado:
#         i += 1
#     else:
#         i -= 1
# atacadas = atacadas.count(1)
# print(atacadas, total)

def jornada_das_estrelas_otimizado(N, carneiros):
    estrelas_atacadas = sum(1 for c in carneiros if c % 2 == 1)
    carneiros_nao_roubados = sum(carneiros) - estrelas_atacadas

    return estrelas_atacadas, carneiros_nao_roubados


# Entradas de exemplo
n = int(input())
x = [int(x) for x in input().split()]

# Chama a função otimizada para obter o resultado
resultado = jornada_das_estrelas_otimizado(n, x)
print(resultado)