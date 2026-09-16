#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.


try:
    #Leitura do número
    numero = float(input('Digite um numero: '))

    #Calculo do dobro
    Dobro = numero * 2

    #Calculo do triplo
    Triplo = numero * 3

    #Calculo de raiz quadrada
    Raiz = numero ** (1/2)

    print(f'O dobro é {Dobro:.1f}\no triplo é {Triplo:.1f}\na raiz quadrada é {Raiz:.1f}.')

except ValueError:
    print('Só aceitamos números')