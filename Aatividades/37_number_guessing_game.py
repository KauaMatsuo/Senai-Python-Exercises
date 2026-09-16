#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.

import random

vezes = 1
aleatorio = random.randint(1, 10)

numero = int(input('Adivinhe o numero entre 1 a 10: '))

while numero != aleatorio:
    numero = int(input('Tente novamente: '))
    vezes += 1

print(f'Voce adivinhou, usou {vezes} tentativas')