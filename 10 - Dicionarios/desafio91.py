# "Jogar 4 dados" e guardar o resultado de cada dado em um dicionario
# Colocar o dicionario em ordem, sabendo que o vencedor fica em 1º, e tem o maior numero de dados

from random import randint
from time import sleep
from operator import itemgetter
jogadas = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
print(f'{" JOGO DOS DADOS ":=^30}\n')
for c in range(1, 5):
    print(f'    O {c}ºJogador tirou {jogadas[f"jogador{c}"]}')
    sleep(1)
print(f'{" RANKING ":=^30}\n')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for c in range(0, 4):
    print(f'    {c + 1}ºLugar - {ranking[c][0]}')
    sleep(1)
