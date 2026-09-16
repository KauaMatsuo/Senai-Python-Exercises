#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.

n1 = float(input('Escreva um numero:'))

if n1 > 20:
    print('É maior que 20')
elif n1 > 10:
    print('Esta entre 10 e 20')
elif n1 > 0:
    print('Esta entre 0 e 10')
else:
    print('Negativo')