valor_n = int(input())
valores = [int(x) for x in input().split()]
is_nlogonia = 1
base = ''
for x in range(valor_n):
    if x == 0:
        if valores[x] == valores[x+1]:
            is_nlogonia = 0
            break
        elif valores[x] < valores[x+1]:
            base = 'menor'
        elif valores[x] > valores[x+1]:
            base = 'maior'
    else:
        if base == 'menor':
            if valores[x-1] > valores[x] or valores[x-1] == valores[x]:
                is_nlogonia = 0
                break
        elif base == 'maior':
            if valores[x-1] < valores[x] or valores[x-1] == valores[x]:
                is_nlogonia = 0
                break
        base = 'maior' if base == 'menor' else 'menor'
print(str(is_nlogonia))