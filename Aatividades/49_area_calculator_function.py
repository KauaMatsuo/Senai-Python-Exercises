#Crie um programa que tenha a função área(), que receba as dimensões de um muro retangular e mostra a área do terreno

base = int(input('digite a base: '))
altura = int(input('digite a altura: '))

def area(base, altura):
    area = base * altura
    print(area)

area(base, altura)
