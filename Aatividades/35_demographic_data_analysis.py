#Escreva um programa que leia o Nome, idade e sexo de 4 pessoas. No final mostre:

#1 - A média de idade do grupo
#2 - Qual é o homem mais velho
#3 - Quantas mulheres têm menos de 20 anos

try:
    nome_homem_velho = ''
    idade_homem_velho = 0
    soma_mulher = 0
    soma = 0


    for cod in range(0, 4):
        nome = input('escreva o nome: ')

        idade = int(input('Digite a idade: '))

        sexo = int(input('Digite:\n'
                     '1 - Masculino\n'
                     '2 - Feminino\n'
                     '\n'
                     '--->: '))

        soma = soma + idade

        if idade > idade_homem_velho and sexo == 1:
            idade_homem_velho = idade
            nome_homem_velho = nome


        if idade < 20 and sexo == 2:
            soma_mulher = soma_mulher + 1

except ValueError:
    print('Só aceitamos números\n')



print(f'1 - A media do grupo é {soma / 4}\n'
      f'2 - O homem mais velho é {nome_homem_velho} e tem {idade_homem_velho}\n'
      f'3 - e tem {soma_mulher} mulheres com menos de 20 anos')


