#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

#peso/(altura x altura)


try:
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))

    altura = altura / 100

    imc = peso / (altura ** 2)

    print(f'Seu imc é {imc:.1f}')

    if imc >= 30:
        print('Obesidade')
    elif imc > 25:
        print('Sobrepeso')
    elif imc > 18.5:
        print('Normal')
    else:
        print('Peso baixo')

except ValueError:
    print('Só aceitamos números\n')
