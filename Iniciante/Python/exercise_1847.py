valor_a, valor_b, valor_c = [int(x) for x in input().split()]

if valor_a > valor_b:
    if valor_c > valor_b:
        print(':)')
    elif valor_b - valor_c < valor_a - valor_b:
        print(':)')
    else:
        print(':(')
elif valor_a < valor_b:
    if valor_c < valor_b:
        print(':(')
    elif valor_b - valor_c > valor_a - valor_b:
        print(':(')
    else:
        print(':)')
elif valor_c > valor_a:
        print(':)')
else:
    print(':(')