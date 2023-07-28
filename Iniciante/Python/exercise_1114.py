def isPasswordValid(number):
    return number == 2002

while isPasswordValid(int(input())) == False:
    print('Senha Invalida')

print('Acesso Permitido')