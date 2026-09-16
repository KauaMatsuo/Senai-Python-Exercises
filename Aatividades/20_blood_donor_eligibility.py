#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.
try:
    idade = int(input('Digite sua idade: '))


    if idade >= 18 and idade <= 60:
        peso = int(input('Digite seu peso: '))
        if peso >= 50 and peso <= 140:
            print('seu peso é bom')
            bebeu = input('ingeriu alguma bebida?: ').strip().lower
            if bebeu in 'naonão':
                print('não bebe')
                humano = input('Você é humano?: ').strip().lower
                if humano in 'sim':
                    print('é humano')
                    tatuagem = input('Fez alguma tatuagem há menos de 6 meses?: ').strip().lower
                    if tatuagem in 'nao não':
                        print('Fique a vontade para doar')
                    else:
                        print('você tem tatuagem, não pode doar')
                else:
                    print('Você não é humano, sai daqui!!!')
            else:
                print('Você bebe, não pode doar')
        else:
            print('Você não tem o peso ideal, não pode doar')
    else:
        print('\nVocê é de menor, não pode doar')

except ValueError:
    print('Só aceitamos números')


'''
if idade and 18:
    print('maior de idade')
elif peso >= 50 <= 140:
    print('seu peso é bom')
elif bebeu in 'nao não':
    print('não bebe')
elif humano == 'sim':
    print('é humano')
elif tatuagem in 'nao não':
    print('não tem tatuagem')
else:
    print('você não pode doar')
    


if idade >= 18 and idade and peso >= 50 and peso < 140 and bebeu in 'nãonao' and humano in 'sim' and tatuagem in 'nãonao':
    print('\nFique a vontade para doar')
else:
    print('\nVocê não pode doar')



if idade >= 18:
    if peso >= 50 <= 140:
        print('seu peso é bom')
        if bebeu in 'naonão':
            print('não bebe')
            if humano in 'sim':
                print('é humano')
                if tatuagem in 'nao não':
                    print('Fique a vontade para doar')
                else
        else:
    else:
else:
    print('\nvocê não pode doar')


'''


