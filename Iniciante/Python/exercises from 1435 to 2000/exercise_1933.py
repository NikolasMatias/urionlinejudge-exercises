carta_1, carta_2 = [int(x) for x in input().split()]
if carta_1 == carta_2:
    print(str(carta_1))
else:
    print(str(max([carta_1, carta_2])))