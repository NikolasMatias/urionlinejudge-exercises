musicas = {
    0: 'PROXYCITY',
    1: 'P.Y.N.G.',
    2: 'DNSUEY!',
    3: 'SERVERS',
    4: 'HOST!',
    5: 'CRIPTONIZE',
    6: 'OFFLINE DAY',
    7: 'SALT',
    8: 'ANSWER!',
    9: 'RAR?',
    10: 'WIFI ANTENNAS'
}

countLoop = int(input())
resultados = [sum([int(y) for y in input().split()[:2]]) for x in range(countLoop)]
for resultado in resultados:
    print(musicas[resultado])