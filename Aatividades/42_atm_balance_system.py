#Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico, permitindo que o usuário faça depósitos, saques e consulte o saldo da conta, e sair
#deposito
#saques
#saldo
#sair

#memoria
digite = ''
maior_n = 0
saldo = 2000
valor = 0


#1
while digite != 4:

    print('-----------------Bem vindo a caixa eletronica----------------------')
    digite = int(input('Digite uma ação abaixo\n1.	sacar\n2.	Depositar\n3.	Ver saldo\n4.	sair\n------>'))

    if digite == 1:
        acao = float(input(f'Seu saldo é {saldo} deseja sacar quantos: '))
        if acao > saldo:
            print('quantidade invalida')
        else:
            valor = saldo - acao
            print(f'voce sacou {valor}')

    elif digite == 2:
        acao = float(input(f'Seu saldo é {saldo} deseja depositar quantos: '))
        if acao > 0:
            valor = saldo + acao
            print(f'voce depositou {acao}, saldo agora é {valor}')
        else:
            print('quantidade invalida')

    elif digite == 3:
        print(f'seu saldo é {saldo}')

    else:
        print('voce saiu')

saldo = valor