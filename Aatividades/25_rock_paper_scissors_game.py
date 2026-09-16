#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random
import time
#Pagina inicial
print('------------------------------------- Bem Vindo ao JOKEMPO -------------------------------------\n')

while True:
    try:
        print('Digite\n1 - pedra\n2 - papel\n3- tesoura\n')


        #comando
        jogador = int(input('----> '))

        #pc
        pc = random.randint(1,3)


        #time
        print('\nJo')
        time.sleep(1)
        print('Kem')
        time.sleep(1)
        print('Po\n')


        #jogada
        print(f'Jogador: {jogador}\n'
              f'Pc: {pc}\n')


        #jogo
        if jogador == pc:
            print('empate')
        elif jogador == 1 and pc == 3:
            print('Você ganhou, pedra vece papel\n')
        elif jogador == 2 and pc == 1:
            print('Você ganhou, papel vence pedra\n')
        elif jogador == 3 and pc == 2:
            print('Você ganhou, tesoura vence papel\n')
        elif pc == 1 and jogador == 3:
            print('Você perdeu, pedra vece papel\n')
            print('Pen')
            time.sleep(0.5)
            print('Peen')
            time.sleep(0.5)
            print('Peeen')
            time.sleep(0.5)
            print('Peeeeeeeen\n')
            time.sleep(0.5)
        elif pc == 2 and jogador == 1:
            print('Você perdeu, papel vence pedra\n')
            print('Pen')
            time.sleep(0.5)
            print('Peen')
            time.sleep(0.5)
            print('Peeen')
            time.sleep(0.5)
            print('Peeeeeeeen\n')
            time.sleep(0.5)
        elif pc == 3 and jogador == 2:
            print('Você perdeu, tesoura vence papel\n')
            print('Pen')
            time.sleep(0.5)
            print('Peen')
            time.sleep(0.5)
            print('Peeen')
            time.sleep(0.5)
            print('Peeeeeeeen\n')
            time.sleep(0.5)
        else:
            print('Valores invalidos')

    except ValueError:
        print('Só aceitamos números\n')
