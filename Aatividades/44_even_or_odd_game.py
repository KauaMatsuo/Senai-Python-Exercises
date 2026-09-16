#Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder. Ao final deve mostrar a quantidade de vitórias

import random

vitorias = 0
perdas = 0

while True:
    print('------------------- impar ou par -------------------')
    humano = input(f'Impar ou par? ').strip().lower()
    numero = int(input(f'Digite um numero de 1 a 10 '))
    pc = random.randint(1, 10)
    soma = numero + pc

    if humano == 'par':
        if soma % 2 == 0:
            print(f'Vc ganhou. pc jogou {pc}')
            vitorias =+ 1
        else:
            print(f'Vc perdeu, pc jogou {pc}')
            perdas = + 1
    elif humano == 'impar':
        if soma % 2 != 0:
            print(f'Vc ganhou. pc jogou {pc}')
            vitorias =+ 1
        else:
            print(f'Vc perdeu, pc jogou {pc}')
            perdas = + 1

    print(f'Voce vendeu {vitorias} vezes, e perdeu {perdas}. ')

    fim = input('Deseja continuar? (sim/nao)').strip().lower()

    if fim == 'naonão':
        break