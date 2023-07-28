numberLoop = int(input())
medias = []

for x in range(numberLoop):
    medias.insert(x, 0)
    valorA, valorB, valorC = [float("{:.1f}".format(float(y))) for y in input().split()]
    medias[x] += valorA * 2
    medias[x] += valorB * 3
    medias[x] += valorC * 5
    medias[x] = medias[x]/10

for x in medias:
    print("{:.1f}".format(x))
