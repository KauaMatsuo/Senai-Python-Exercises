#Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

palavra = input('Escreva uma palavra: ').strip().lower()

if palavra[0] in 'aeiou':
    print(f'A primeira palavra é uma vogal')
else:
    print('A primeira palavra é uma consoante')