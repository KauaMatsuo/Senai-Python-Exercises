#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

letra = input('Digite uma letra: ').strip().lower()


if letra[0] in 'aeiou':
    print('é vogal')
else:
    print('é consoante')