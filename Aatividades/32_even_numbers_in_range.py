#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.
try:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))

    for pares in range(n1, n2 + 1):
        if pares % 2 == 0:
            print(pares)

except ValueError:
    print('Só aceitamos números\n')

