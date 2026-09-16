#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

try:
    numero = int(input('Escreva um numero:'))

    if numero % 2 == 0:
        print('Seu numero é par')
    else:
        print('Seu numero é impar')

except ValueError:
    print('Só aceitamos números')

