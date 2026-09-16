#Crie um programa que leia uma frase e mostre:
#1 - Quantas vezes aparece a letra “a”
#2 - Em que posição ela aparece a primeira vez
#3 - Em que posição ela aparece na última vez

frase = input('escreva uma frase: ').strip().lower()

print(f'A letra "a" aparece {frase.count("a")} vezes'
      f'A letra a aparece pela primeira vez: {frase.find("a")}'
      f'A letra a aparece pela ultima vez: {frase.rfind("a")}')
