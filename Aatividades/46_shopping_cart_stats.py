#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000,00
#Qual é o produto mais barato

fim = ''
mais = 0
total_g = 0

while True:

    if fim == 'S':
        print(f'total gasto é: R${total_g}\n'
              f'{mais} produtos, que custa mais que R$1000\n'
              f'produto mais barato é {nome_1}, que custa R${preco_b}')
        break

    nome = input('\nEscreva o nome do produto: ')


    #total gasto
    preco = int(input('Digite o preço do produto: '))

    total_g += preco

    #mais de 1000
    if preco > 1000:
        mais =+ 1

    #produto mais barato
    nome_1 = nome
    preco_b = preco

    if preco < preco_b:
        nome_1 = nome
        preco_b = preco

    fim = input('\nDigite (S) se quiser parar [S/N]: ').strip().upper()




