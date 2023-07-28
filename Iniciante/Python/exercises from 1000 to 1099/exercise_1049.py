vertebra = str(input())
tipo = str(input())
alimentacao = str(input())

resultados = {
    'vertebrado': {
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba'
        },
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca'
        }
    },
    'invertebrado': {
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        },
        'anelideo': {
            'hematofago': 'sanguessuga',
            'onivoro': 'minhoca'
        }
    }
}

if vertebra in resultados:
    if tipo in resultados[vertebra]:
        if alimentacao in resultados[vertebra][tipo]:
            print(resultados[vertebra][tipo][alimentacao])