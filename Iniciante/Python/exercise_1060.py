numbers = []
count = 0

for x in range(6):
    if float(input()) >= 0:
        count += 1

print(''.join([str(count), ' valores positivos']))