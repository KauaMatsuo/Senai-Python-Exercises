#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

try:
    numero = float(input('Escreva um numero:'))

    if numero > 0:
        print('Numero positivo')
    else:
        print('Numero negativo')

except ValueError:
    print('Só aceitamos números')