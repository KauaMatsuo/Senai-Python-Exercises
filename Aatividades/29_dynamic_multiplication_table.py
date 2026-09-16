#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

try:
    numero = int(input('Digite um numero: '))

    #for ele in range(1, 11):

    n2 = 0

    for ele in range(1,11):
        n2 = n2 + 1
        resultado = numero * n2
        print(f'{numero} X {n2} = {resultado}')

except ValueError:
    print('Só aceitamos números\n')

