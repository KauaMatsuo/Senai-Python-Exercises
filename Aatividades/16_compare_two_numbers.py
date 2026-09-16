#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.


try:

    n1 = float(input('Escreva um numero:'))

    n2 = float(input('Escreva outro numero:'))

    if n1 == n2:
        print('Os dois numeros são iguais')
    else:
        print('Os dois são diferentes')

except ValueError:
    print('Só aceitamos números')