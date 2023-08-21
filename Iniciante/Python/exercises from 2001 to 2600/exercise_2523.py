while True:
    try:
        characters = list(input())[:26]
        countLoop = int(input())
        indices = [int(x) for x in input().split()[:countLoop]]
        print(''.join([characters[indice-1] for indice in indices]))
    except EOFError: break