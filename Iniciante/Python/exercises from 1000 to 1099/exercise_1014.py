distancia = int(input())
cosbustivel = float(input())

consumoMedio = distancia/cosbustivel

print(''.join([ "{:.3f}".format(consumoMedio), ' km/l']))