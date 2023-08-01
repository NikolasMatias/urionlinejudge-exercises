def is_triangle(valor_a, valor_b, valor_c):
    is_A_plus_B_bigger_than_C = valor_a+valor_b > valor_c
    is_B_plus_C_bigger_than_A = valor_b+valor_c > valor_a
    is_A_plus_C_bigger_than_B = valor_a+valor_c > valor_b
    return is_A_plus_C_bigger_than_B and is_B_plus_C_bigger_than_A and is_A_plus_B_bigger_than_C

valor_a, valor_b, valor_c, valor_d = [int(x) for x in input().split()]

if (is_triangle(valor_a, valor_b, valor_c)
        or is_triangle(valor_a, valor_b, valor_d)
        or is_triangle(valor_a, valor_c, valor_d)
        or is_triangle(valor_b, valor_c, valor_d)):
    print('S')
else:
    print('N')