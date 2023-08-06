while True:
    compra, pago = [int(x) for x in input().split()]
    if compra == 0 and pago == 0:
        break
    troco = pago - compra
    notas = [100, 50, 20, 10, 5, 2]
    qtde_notas = 0
    for nota in notas:
        qtde_notas += troco // nota
        troco = troco % nota
    if qtde_notas == 2:
        print('possible')
    else:
        print('impossible')