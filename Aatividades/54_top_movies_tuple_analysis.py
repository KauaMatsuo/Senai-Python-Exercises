#Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

#Apenas os 3 primeiros mais assistidos
#Os últimos 2 mais assistidos
#A lista em ordem alfabética
#Em que posição está “O rei leão”

filmes = ('Homem Aranha', 'Homem de ferro', 'Velozes e furiozes', 'Toy story', 'Vingadores', 'O rei leão', 'Jurassic World', 'Titanic', 'Avatar', 'Star Wars')

print(filmes)

for i in range(0, 3):
    print(filmes[i])

for i in range(-1, -3, -1):
    print(filmes[i])

print(sorted(filmes))


print(f'Rei leão esta na posição {filmes.index("O rei leão") + 1}')

