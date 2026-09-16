#Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário

#Leitura
posicao_inicial = float(input('Escreva a posicção inicial: '))
velocidade_inicial = float(input('Escreva a velocidade inicial: '))
aceleracao = float(input('Escreva a aceleração: '))
instante_de_tempo = float(input('Escreva o instante de tempo: '))

#Posição final
posicao = posicao_inicial + (velocidade_inicial * instante_de_tempo) + ((aceleracao * instante_de_tempo ** 2) / 2)

#Retorno ao usuario
print(f'A posição do objeto no tempo {instante_de_tempo} é de {posicao} (m)')