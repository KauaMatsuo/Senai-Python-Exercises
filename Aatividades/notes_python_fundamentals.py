'''
# Operações Matemáticas :)
print(85 * 8)
print(1 + 1)
print(5 - 2)
print(5 * 2)
print(10 / 5)
print(2 ** 2)
print(1024 ** 98)

# Retorno de Texto
print('Bem vindo ao senai')

#Variáveis
idade_kaua = 92
altura = 1.20

idade_Joao = 8

Soma_idades = idade_Joao + idade_kaua

print(f'A soma da idades é {Soma_idades}')

Nome = input('Digite seu nome: ')
print(f'Seu nome é {Nome}')

#Concatenação de Strings
Nome = 'Kauã'
Sobrenome = 'Kenzo'

Nome_Completo = Nome + Sobrenome

print(Nome_Completo)

idade_1 = int(input('Digite a sua idade: '))
idade_2 = int(input('Digite a sua idade: '))

Soma = idade_1 + idade_2

print(Soma)


#strings
nome = 'Luis Tatin'
print(nome[0])
print(nome[0:5])
print(nome[:10])
print(nome[9:])

print(len(nome))
print(nome.count('i'))
print(nome.replace('L' , 'P'))
print(nome.upper())
print(nome.lower)

nome = input('Digite seu nome: ').strip()
print(nome)

nome = input('Digite seu nome: ').strip().split()
print(nome)


altura = float(input('Digite a sua altura: '))

if altura > 2:
    print('Cuidado você cai bater a cabeça!!!')

elif altura < 1.4:
    print('Quem sabe no ano que vem')

else:
    print('Pode entrar no brinquedo')


import random

aleatorio = random.randint(1,6)


for ele in range(1, 10):
    print('*')

for ele in range(0, 10):
    print(ele)

for ele in range(10, 0, -1):
    print(ele)

soma = 0
for ele in range(0, 5):
    numero = int(input('digite um número: '))
    soma = soma + numero

print(soma)

#while

#numerio

contador = a

while contador < 10:
    print(contador)
    contador += 1
    #contador = contador = 1

#texto

resposta = ''
 while resposta!= 'N':
     print('Oi')
     resposta = input('Deseja Continuar? [S/N] ----->').strip().upper()


while True:
    escolhas = int(input('1.....'
                         '\n2.....'
                         '\n3......'))
    if escolhas == 3:
        break

#condição de parada em cima, para na hora
#condição de parada em baixo, roda até acabar



while True:
    try:
        numero = int(input('Digite um número: '))
        x = 10 / 0

    except ValueError:
        print('Só aceitamos números')

    except ZeroDivisionError:
        print('Não dividimos por zero')



#1 caso

def quebra_linha():
    print('***' * 30)


quebra_linha()
numero = int(input('Digite aldo: '))
quebra_linha()

#2 caso

def titulo(msg):
    print('---' * 30)
    print(msg)
    print('---' * 30)

titulo('Exercicio 50')

#3 caso

def IMC(peso, altura):

    resultado = peso/(altura ** 2)

    return resultado
IMC_pedro = IMC(70, 1.90)

print(IMC_pedro)
'''

carro = ('Ferrari', 'Vermelha', '2023')
print(carro)

for ele in carro:
   print(ele)

for count in range(0, len(carro)):
   print(carro[count])

for pos, carac in enumerate(carro):
   print(f'Ordem de compra {carac} Cod: {pos}')
