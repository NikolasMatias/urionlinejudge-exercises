while True:
    try:
        num_gameplays, my_id = [int(x) for x in input().split()]
        gameplays = [[int(y) for y in input().split()[:2]] for x in range(num_gameplays)]
        myCSPlays = sum([1 if gameplay[0] == my_id and gameplay[1] == 0 else 0 for gameplay in gameplays])
        print(str(myCSPlays))
    except EOFError: break