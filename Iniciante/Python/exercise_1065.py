count = 0

for x in range(5):
    if int(input())%2 == 0:
        count += 1

print(''.join([str(count), ' valores pares']))