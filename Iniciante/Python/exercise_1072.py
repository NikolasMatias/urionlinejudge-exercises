countIn = 0
countOut = 0
numberLoops = int(input())

for x in range(numberLoops):
    number = int(input())
    if number >= 10 and number <= 20:
        countIn += 1
    else:
        countOut += 1

print(''.join([str(countIn), ' in']))
print(''.join([str(countOut), ' out']))