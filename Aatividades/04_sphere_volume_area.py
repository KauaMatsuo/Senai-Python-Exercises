#screva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
#V = (4/3) . π . r³
#A = 4 . π . r²

try:
    raio = float(input('Escreva o raio para saber o volume: '))

    Volume_calculo = ((4/3) * 3.1415 * raio**3)
    Base_calculo = (4 * 3.1415 * raio**2)

    print(f'O volume é: {Volume_calculo} \nE a base é: {Base_calculo}')

except ValueError:
    print('Só aceitamos números')