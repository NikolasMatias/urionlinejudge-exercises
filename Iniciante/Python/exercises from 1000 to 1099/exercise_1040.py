nota1, nota2, nota3, nota4 = [float("{:.1f}".format(float(x))) for x in input().split()]

media = (nota1*2+nota2*3+nota3*4+nota4*1)/10

print(''.join(['Media: ', "{:.1f}".format(media)]))

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif media >= 5 and media < 7:
    print('Aluno em exame.')

    notaExame = float("{:.1f}".format(float(input())))
    print(''.join(['Nota do exame: ', "{:.1f}".format(notaExame)]))

    media = (media+notaExame)/2

    if media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(''.join(['Media final: ', "{:.1f}".format(media)]))