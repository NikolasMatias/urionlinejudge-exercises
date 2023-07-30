import math
countLoop = int(input())

for x in range(countLoop):
    base, expoente = [int(y) for y in input().split()]
    digits = int(math.log10(base**expoente))+1
    print(str(digits))