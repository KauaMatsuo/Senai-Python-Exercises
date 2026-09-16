'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome'''

#leitura
nome = input('digite seu nome completo: ').strip()


#3.1 - Resmover espaços
quantidade_de_letras = len(nome.replace(' ' , ''))

#3.1 - Resmover espaços
quantidade_de_letras = len(nome) - nome.count(' ')

#4.0
primeiro_espaco = nome.find(' ')
quantidade_de_letras_primeiro_nome = len(nome[:primeiro_espaco])

#retorno ao usuario
print(f'Com todas as letras Maiusculas: {nome.upper()}'
      f'\nCom todas as letras Minusculas: {nome.lower()}'
      f'\nQuantidade de letras sem espaço: {quantidade_de_letras}'
      f'\nquantidade de letras no primeiro nome: {quantidade_de_letras_primeiro_nome}')



