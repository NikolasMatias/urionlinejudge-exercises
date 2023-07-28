numberLoop = int(input())
countCoelhos = 0
countRatos = 0
countSapos = 0

for x in range(numberLoop):
    qtde, tipo = input().split()

    if tipo == 'C':
        countCoelhos += int(qtde)
    elif tipo == 'S':
        countSapos += int(qtde)
    elif tipo == 'R':
        countRatos += int(qtde)

total = countCoelhos + countSapos + countRatos

print(''.join(['Total: ', str(total), ' cobaias']))
print(''.join(['Total de coelhos: ', str(countCoelhos)]))
print(''.join(['Total de ratos: ', str(countRatos)]))
print(''.join(['Total de sapos: ', str(countSapos)]))
print(''.join(['Percentual de coelhos: ', "{:.2f}".format((countCoelhos*100)/total), ' %']))
print(''.join(['Percentual de ratos: ', "{:.2f}".format((countRatos*100)/total), ' %']))
print(''.join(['Percentual de sapos: ', "{:.2f}".format((countSapos*100)/total), ' %']))