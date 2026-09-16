#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

#Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

saldo = 1200
troco = 0
cinquenta = 50
vinte = 20
dez = 10
um = 1

while True:
    saque = int(input('deseja sacar quantos: '))


    if saldo == 0:
        print('Seu saldo esta zerado')
    elif saque > saldo:
        print(f'digite um valor valido, seu saldo é {saldo}')
    else:
        sacado = saldo - saque

        troco_cinquenta = 0
        troco_vinte = 0
        troco_dez = 0
        troco_um = 0

        if sacado % cinquenta == 0 :
            troco_cinquenta = sacado / 50
        elif sacado % vinte == 0:
            troco_vinte = sacado / 20
        elif sacado % dez == 0:
            troco_dez = sacado / 10
        elif sacado % um == 0:
            troco_um = sacado / 1


        print(f'voce sacou R${sacado}\n'
              f'Seu troco terá:\n'
              f'{troco_cinquenta} notas de R$50\n'
              f'{troco_vinte} notas de R$20\n'
              f'{troco_dez} notas de R$10\n'
              f'{troco_um} notas de R$1')

