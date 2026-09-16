#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

#1.	Somar
#2.	Multiplicar
#3.	Maior
#4.	Novos números
#5.	Sair do programa

#memoria
digite = ''
maior_n = 0


#entrada
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))


#1
while digite != 5:

    print('---------------------------------------')
    digite = int(
        input('\n1.	Somar\n2.	Multiplicar\n3.	Maior\n4.	Novos números\n5.	Sair do programa\n------>'))

    if digite == 1:
        print(f'A soma da {n1 + n2 + n3}')
        print('Digite 5 se quiser parar: ')

    elif digite == 2:
        print(f'A multiplicação da {n1 * n2 * n3}')
        print('Digite 5 se quiser parar: ')

    elif digite == 3:
        if n1 > n2 and n1 > n3:
            maior_n = n1
            print(f'maior é {maior_n}')
            print('Digite 5 se quiser parar: ')
        elif n2 > n3 and n2 > n1:
            maior_n = n2
            print(f'maior é {maior_n}')
            print('Digite 5 se quiser parar: ')
        elif n3 > n2 and n3 > n1:
            maior_n = n3
            print(f'maior é {maior_n}')
            print('Digite 5 se quiser parar: ')

    elif digite == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
        n3 = int(input('Digite um numero: '))






