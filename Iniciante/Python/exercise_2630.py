from math import floor
cases = int(input())
for x in range(cases):
    tipo = input()
    rgb = [int(y) for y in input().split()[:3]]
    print(''.join(['Caso #', str(x+1), ': ']), end='')
    if tipo == 'eye':
        red, green, blue = rgb
        valor_p = 0.3*red + 0.59*green + 0.11*blue
        print(str(floor(valor_p)))
    elif tipo == 'min':
        print(str(min(rgb)))
    elif tipo == 'max':
        print(str(max(rgb)))
    elif tipo == 'mean':
        print(str(floor(sum(rgb)/len(rgb))))