import math
valor_n = int(input())
valor_p = valor_n/math.log(valor_n)
valor_m = 1.25506*valor_p
print('{:.1f}'.format(valor_p), '{:.1f}'.format(valor_m))