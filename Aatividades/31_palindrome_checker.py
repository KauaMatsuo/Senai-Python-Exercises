#Escreva um programa que verifique se uma frase é um palíndromo.


palavra = input('Digite um políndromo: ').strip()

compatibilidade = 0


soma = 0

for ele in range(0, len(palavra)):


    if palavra[ele] == palavra[-ele - 1]:
        compatibilidade = compatibilidade + 1

if compatibilidade == len(palavra):
    print('é um palíndromo')
else:
    print('Não um palíndromo')

#2
if palavra == palavra[::-1]:
    print('sim')
else:
    print('nao')