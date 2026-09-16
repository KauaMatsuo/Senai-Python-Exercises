#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois, deve mostrar para cada palavra, suas vogais

palavras = ('milho', 'paralelepipedo', 'celular', 'notebook', 'otorinolaringologista', 'sara')



for palavra in palavras:
    print(f'\n\n{palavra}')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')

