#Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos).



try:
    idade = int(input('Escreva um numero:'))

    if idade >= 18:
        print('Você é maior de idade')
    else:
        print('Você é menor de idade')

except ValueError:
    print('Só aceitamos números')