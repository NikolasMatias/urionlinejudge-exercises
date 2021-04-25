def isPrime(n) :

    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

resultado = 4

while not isPrime(resultado):
    try:
        quantidadeDeMoeda = int(input())
    except EOFError as e:
        print(e)
    moedas = []

    increment = 0
    while increment < quantidadeDeMoeda:
        try:
            moedas.append(int(input()))
        except EOFError as e:
            print(e)
        increment+=1

    try:
        saltoNaSoma = int(input())
    except EOFError as e:
        print(e)


    somaMoedas = 0
    increment = 0

    decrementSoma = len(moedas)-1

    while decrementSoma >= 0:
        somaMoedas+=moedas[decrementSoma]

        increment+=1
        decrementSoma=(len(moedas)-1)-(saltoNaSoma*increment)

    resultado = somaMoedas

    if not isPrime(resultado):
        print("Bad boy! I’ll hit you.")

print("You’re a coastal aircraft, Robbie, a large silver aircraft.")