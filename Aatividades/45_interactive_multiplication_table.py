#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000



while True:
    numero = input('Digite um numero: ')

    if numero == '0000':
        print('voce saiu')
        break


    for ele in range(1, 11):
        resultado = int(numero) * ele
        print(f'{numero} X {ele} = {resultado}')

    numero = input(f'Continue ou digite 0000 para sair: ')



