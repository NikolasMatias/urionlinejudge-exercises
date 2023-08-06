while True:
    try:
        count_lesmas = int(input())
        lesmas = [int(x) for x in input().split()]
        maior_velocidade = max(lesmas)
        if maior_velocidade < 10:
            print('1')
        elif maior_velocidade >= 10 and maior_velocidade < 20:
            print('2')
        elif maior_velocidade >= 20:
            print('3')
    except EOFError:
        break