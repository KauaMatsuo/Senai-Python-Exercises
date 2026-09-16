#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos


try:
    maior_peso = 0
    menor_peso = maior_peso

    for ele in range(0, 7):
        peso = int(input('Digite o peso: '))

        if peso < menor_peso:
            menor_peso = peso

    print(f'O menor peso é {menor_peso}')

except ValueError:
    print('Só aceitamos números\n')