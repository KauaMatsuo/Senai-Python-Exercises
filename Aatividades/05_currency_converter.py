#Escreva um programa que converta real para o Franco Congolês : 0,0019


try:
    #leitura
    Real = (float(input('Escreva o real: ')))

    #Calculo de converção
    Convertido = Real * 539.62

    print(f'{Real} R$ ficará {Convertido:.2f} CDF')

except ValueError:
    print('Só aceitamos números')