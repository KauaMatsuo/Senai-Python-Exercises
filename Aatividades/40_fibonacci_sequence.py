#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

numero = int(input('Digite o numero de elementos: '))

i = 0
prox = 0
ant = 0
atual = 0


while i < numero:
    if i == 0:
        atual = 0

    if i == 1 or i == 2:
        atual = 1
        ant = 0

    prox = ant + atual
    ant = atual
    atual = prox

    print(atual)
    i = i + 1

