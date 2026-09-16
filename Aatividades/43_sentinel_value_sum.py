#Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000. No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)


quantidade = 0
soma = 0

while True:
    numero = input('Digite um numero (digite 0000 para sair: ')

    if numero == '0000':
        break

    quantidade += 1
    soma = soma + int(numero)

print(f'Foram digitados {quantidade} vezes, e a soma é {soma}')