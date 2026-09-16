#Crie um programa que leia um nome, e mostre o primeiro e o último nome

#Entrada
nome = input('digite seu nome completo: ').strip()

#segundo nome
primeiro_espaco = nome.find(' ')
primeiro_nome = nome[:primeiro_espaco]


#primeiro nome
ultimo_espaco = nome.rfind(' ')
segundo_nome = (nome[ultimo_espaco + 1:])


#2
nome = nome.split()
print(nome[0])
print(nome[len(nome) - 1])


#3
print(nome[0])
print(nome[-1])


#retorno
print(nome)
print(primeiro_nome.capitalize())
print(segundo_nome.capitalize())
