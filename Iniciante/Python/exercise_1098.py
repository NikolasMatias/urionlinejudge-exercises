def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

valorI = 0
valorJ1 = 1
valorJ2 = 2
valorJ3 = 3

# "{:.1f}".format

while valorI <= 2:
    print(''.join(['I=', str(int(valorI)) if is_integer_num(valorI) else "{:.1f}".format(valorI), ' J=', str(int(valorJ1)) if is_integer_num(valorJ1) else "{:.1f}".format(valorJ1)]))
    print(''.join(['I=', str(int(valorI)) if is_integer_num(valorI) else "{:.1f}".format(valorI), ' J=', str(int(valorJ2)) if is_integer_num(valorJ2) else "{:.1f}".format(valorJ2)]))
    print(''.join(['I=', str(int(valorI)) if is_integer_num(valorI) else "{:.1f}".format(valorI), ' J=', str(int(valorJ3)) if is_integer_num(valorJ3) else "{:.1f}".format(valorJ3)]))
    valorI = float("{:.1f}".format(valorI+0.2))
    valorJ1 = float("{:.1f}".format(valorJ1+0.2))
    valorJ2 = float("{:.1f}".format(valorJ2+0.2))
    valorJ3 = float("{:.1f}".format(valorJ3+0.2))