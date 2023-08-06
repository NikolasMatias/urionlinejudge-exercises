altura_pulo, num_canos = [int(x) for x in input().split()]
canos = [int(x) for x in input().split()]
isWinner = True

for x in range(1, num_canos):
    if canos[x-1]+altura_pulo < canos[x]:
        isWinner = False
        break
    if canos[x-1]-canos[x] > 0 and canos[x-1]-canos[x] > altura_pulo:
        isWinner = False
        break
if isWinner:
    print('YOU WIN')
else:
    print('GAME OVER')