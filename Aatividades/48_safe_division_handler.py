#Crie um programa que pede ao usuário para digitar dois números e, em seguida, divide o primeiro número pelo segundo número. No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.


fim = 'sim'

while True:
    try:

        numero_1 = int(input('Número: '))
        numero_2 = int(input('Dividido por: '))

        divisão = numero_1 / numero_2

        print(f'A divisão de {numero_1} e {numero_2} é {divisão}')

        fim = input('Deseja parar (sim ou não): ')

        if fim == 'sim':
            break


    except ZeroDivisionError:
        print('Não dividimos por zero')

    except ValueError:
        print('Só aceitamos números')