credito_a, credito_b, credito_c = [int(x) for x in input().split()]
if credito_a == credito_b or credito_b == credito_c or credito_a == credito_c:
    print('S')
elif (credito_a+credito_b) == credito_c or (credito_a+credito_c) == credito_b or (credito_b+credito_c) == credito_a:
    print('S')
else:
    print('N')