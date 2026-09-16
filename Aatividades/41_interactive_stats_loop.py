#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

#Media
#Maior
#Menor

fim = ''
ciclos = 0
media = 0
maior = 0
menor = 0
numero = 0


while fim != 'N':
    numero = int(input('Digite um numero: '))
    fim = input('Deseja continuar [S/N]: ').strip().upper()
    media = media + numero
    ciclos = ciclos + 1

    if ciclos == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f'A medie é: {media / ciclos}\n'
      f'O marior é: {maior}\n'
      f'O menor é: {menor}')

