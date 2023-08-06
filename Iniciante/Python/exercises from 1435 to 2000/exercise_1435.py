while True:
    countLoop = int(input())
    if countLoop == 0:
        break

    for x in range(countLoop):
        for y in range(countLoop):
            baseX = x+1
            baseY = y+1
            baseValue = x
            if y < x:
                baseValue = y
            baseValue += 1

            if (countLoop - baseX + 1) < baseValue:
                baseValue = countLoop - baseX + 1

            if (countLoop - baseY + 1) < baseValue:
                baseValue = countLoop - baseY + 1

            print('{:3d}'.format(baseValue), end='')
            if baseY < countLoop:
                print(' ', end='')
            else:
                print('')
    print('')