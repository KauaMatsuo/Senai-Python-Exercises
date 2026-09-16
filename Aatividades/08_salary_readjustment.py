#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.


try:

    #leitura
    salario = float(input('Digite seu salário para reajuste: '))

    #calculo de reajuste
    reajuste = 60 / 100 * salario + salario

    print(f'Seu salário com reajuste de 60% é {reajuste:.2f}')

except ValueError:
    print('Só aceitamos números')