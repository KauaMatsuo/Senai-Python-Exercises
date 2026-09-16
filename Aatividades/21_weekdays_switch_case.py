#Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).
try:

    n1 = int(input('Digite um numero de 1 a 7:'))

    if n1 == 1:
        print('Domingo')
    elif n1 == 2:
        print('Segunda-feira')
    elif n1 == 3:
        print('Terça-feira')
    elif n1 == 4:
        print('Quarta-feira')
    elif n1 == 5:
        print('Quinta-feira')
    elif n1 == 6:
        print('sexta-feira')
    elif n1 == 7:
        print('Sabado')
    else:
        print('Digite um numero valido')

except ValueError:
    print('Só aceitamos números')