count_c = int(input())
for x in range(count_c):
    nome, forca = input().split()
    nome = str(nome)
    if nome.lower() == 'thor':
        print('Y')
    else:
        print('N')
