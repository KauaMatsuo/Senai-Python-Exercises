#Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500

soma = 0

for numero in range(1, 501):
    if numero % 4 == 0:
        soma = soma + numero

print(soma)
