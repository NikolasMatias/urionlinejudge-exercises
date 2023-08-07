while True:
    valor_aumento, exp_monstro = [int(x) for x in input().split()]
    if valor_aumento == 0 and exp_monstro == 0:
        break
    print(str(valor_aumento*exp_monstro))