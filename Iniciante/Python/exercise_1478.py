def find_base(x, y):
    base_count = min([x,y])
    base_x = x - base_count
    base_y = y - base_count
    return base_x+base_y+1

while True:
    countLoop = int(input())
    if countLoop == 0:
        break
    for x in range(countLoop):
        for y in range(countLoop):
            print('{:3d}'.format(find_base(x, y)), end='')
            if (y+1) < countLoop:
                print(' ', end='')
            else:
                print('')
    print('')