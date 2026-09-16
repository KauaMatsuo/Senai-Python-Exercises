#Escreva um programa que tenha uma função, verifica_par(), que receba um número e verifique se é par

numero = int(input('Digite um numero inteiro: '))

def verifica_par():
    if numero % 2 == 0:
        print('Seu numero é par')
    else:
        print('Seu numero é impar')


verifica_par()