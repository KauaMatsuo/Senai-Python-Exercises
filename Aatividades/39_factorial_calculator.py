#Faça um programa que leia um número e retorne o fatorial !

#4! = 4 x 3 x 2 x 1


digite = int(input('Digite um numero: '))

i = 1
fat = 1

while i != digite:
    fat = i * fat
    i += 1

print(f'O fatorial de {digite} é {fat}')
