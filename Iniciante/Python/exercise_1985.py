num_products = int(input())
products_type = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}
order = []
for x in range(num_products):
    codigo, qtde_produto = [int(y) for y in input().split()]
    order.append(products_type[codigo]*qtde_produto)
print('{:.2f}'.format(sum(order)))