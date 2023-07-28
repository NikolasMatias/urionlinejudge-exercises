class Lanche:
    def __init__(self, codigo, especificacao, preco):
        self.codigo = codigo
        self.especificacao = especificacao
        self.preco = preco

    def getCodigo(self):
        return self.codigo
    def totalPorQtde(self, qtde):
        return self.preco*qtde


lanches = [
    Lanche(1, 'Cachorro Quente', 4.00),
    Lanche(2, 'X-Salada', 4.50),
    Lanche(3, 'X-Bacon', 5.00),
    Lanche(4, 'Torrada simples', 2.00),
    Lanche(5, 'Refrigerante', 1.50)
]

codigo, qtde = [int(x) for x in input().split()]

for lanche in lanches:
    if codigo == lanche.getCodigo():
        print(''.join(['Total: R$ ', "{:.2f}".format(lanche.totalPorQtde(qtde))]))
        break