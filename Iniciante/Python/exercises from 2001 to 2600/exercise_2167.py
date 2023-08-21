count_velocidades = int(input())
valores = [int(x) for x in input().split()]
index = 0
for x in range(1, count_velocidades):
    if valores[x-1] > valores[x]:
        index = x+1
        break
print(str(index))