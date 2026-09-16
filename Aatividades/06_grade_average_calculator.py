#Escreva um programa que leia 6 notas diferentes e faça a média do aluno


try:
    Aluno = input('Escreva o nome do aluno: ')


    Nota1 = float(input(f'Escreva a 1º nota do {Aluno}: '))
    Nota2 = float(input(f'Escreva a 2º nota do {Aluno}: '))
    Nota3 = float(input(f'Escreva a 3º nota do {Aluno}: '))
    Nota4 = float(input(f'Escreva a 4º nota do {Aluno}: '))
    Nota5 = float(input(f'Escreva a 5º nota do {Aluno}: '))
    Nota6 = float(input(f'Escreva a 6º nota do {Aluno}: '))


    Media = int(Nota1 + Nota2 + Nota3 + Nota4 + Nota5 + Nota6) / 6

    print(f'A média dos alunos foi {Media}')

except ValueError:
    print('Só aceitamos números')