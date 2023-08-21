while True:
    try:
        num_materias = int(input())
        notas_cargas = [[int(y) for y in input().split()[:2]] for x in range(num_materias)]
        nota_ira = sum([notas[0]*notas[1] for notas in notas_cargas])/(sum([cargas[1] for cargas in notas_cargas])*100)
        print('{:.4f}'.format(nota_ira))
    except EOFError: break