count = 0
media = 0

for x in range(6):
    number = float(input())
    if number >= 0:
        count += 1
        media += number

media = media/count

print(''.join([str(count), ' valores positivos']))
print("{:.1f}".format(media))