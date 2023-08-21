def get_only_numbers(string):
    return ''.join(filter(lambda char: char.isdigit(), string))
def get_only_alpha(string):
    return ''.join(filter(lambda char: not char.isdigit(), string))

def analize_qtde_vitamina_c(qtde_vitamina_c):
    if qtde_vitamina_c >  130:
        print(' '.join(['Menos', str(qtde_vitamina_c - 130), 'mg']))
    elif qtde_vitamina_c < 110:
        print(' '.join(['Mais', str(110 - qtde_vitamina_c), 'mg']))
    else:
        print(' '.join([str(qtde_vitamina_c), 'mg']))

alimentos_ricos_vitamina_c = {
    'suco de laranja': 120,
    'morango fresco': 85,
    'mamao': 85,
    'goiaba vermelha': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34
}
qtde_alimentos = int(input())
while qtde_alimentos > 0:
    alimentos = [input() for x in range(qtde_alimentos)]
    qtde_vitamina_c = 0
    for alimento in alimentos:
        qtde_alimento = int(get_only_numbers(alimento))
        nome_alimento = str(get_only_alpha(alimento)).strip()
        qtde_vitamina_c += alimentos_ricos_vitamina_c[nome_alimento]*qtde_alimento
    analize_qtde_vitamina_c(qtde_vitamina_c)
    qtde_alimentos = int(input())