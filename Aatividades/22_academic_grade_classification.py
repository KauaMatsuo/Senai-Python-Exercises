#Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média, é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).


try:
    print('Digite as notas de 0 a 10\n')

    n1 = int(input('Digite a 1º nota: '))
    n2 = int(input('Digite a 2º nota: '))
    n3 = int(input('Digite a 3º nota: '))
    n4 = int(input('Digite a 4º nota: '))
    n5 = int(input('Digite a 5º nota: '))


    media = n1 + n2 + n3 + n4 + n5 / 5

    print(f'A media das notas é {media}')

    if media > 9:
        print('Excelente')
    elif media > 7:
        print('Bom')
    elif media > 6:
        print('Suficiente')
    else:
        print('Insuficiente')

except ValueError:
    print('Só aceitamos números\n')

