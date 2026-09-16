#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário

try:
    #Leitura de Variável
    Nome = input('Escreva seu nome: ')
    Idade = int(input('Escreva sua idade: '))
    Cidade = input('Escreva sua cidade de nascimento: ')

    #Retorno para o Usuario
    print(f'Seu nome é {Nome}')
    print(f'Sua idade é {Idade}')
    print(f'Sua cidade natal é {Cidade}')

except ValueError:
    print('Só aceitamos números')