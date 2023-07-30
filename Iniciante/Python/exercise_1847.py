def calculateResult(valor_a, valor_b, valor_c):
    possibilities = [
        {
            'result': lambda: valor_a > valor_b and valor_b < valor_c,
            'answer': ':)'
        },
        {
            'result': lambda: valor_a < valor_b and valor_b > valor_c,
            'answer': ':('
        },
        {
            'result': lambda: valor_a < valor_b and valor_b < valor_c and (valor_c-valor_b < valor_b-valor_a),
            'answer': ':('
        },
        {
            'result': lambda: valor_a < valor_b and valor_b < valor_c and (valor_c-valor_b >= valor_b-valor_a),
            'answer': ':)'
        },
        {
            'result': lambda: valor_a > valor_b and valor_b > valor_c and (valor_b-valor_c < valor_a-valor_b),
            'answer': ':)'
        },
        {
            'result': lambda: valor_a > valor_b and valor_b > valor_c and (valor_b-valor_c > valor_a-valor_b),
            'answer': ':('
        },
        {
            'result': lambda: valor_a == valor_b and valor_b < valor_c,
            'answer': ':)'
        },
        {
            'result': lambda: valor_a == valor_b and valor_b > valor_c,
            'answer': ':('
        }
    ]
    for possibility in possibilities:
        if possibility['result']():
            return possibility['answer']

valor_a, valor_b, valor_c = [int(x) for x in input().split()]
print(calculateResult(valor_a, valor_b, valor_c))