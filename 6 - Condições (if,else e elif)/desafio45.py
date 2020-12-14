# um jogo que jogue jokenpô

from random import randint
from time import sleep
import emoji

# variaveis com os emogis
emoji_pedra = emoji.emojize(':fist:', use_aliases=True)
emoji_papel = emoji.emojize(':hand:', use_aliases=True)
emoji_tesoura = emoji.emojize(':v:', use_aliases=True)

# Menu
print('====Vamos jogar jókenpô?====')
print('escolha sua jogada')
print('''\033[31m1\033[m -> PEDRA {}
\033[31m2\033[m -> PAPEL {}
\033[31m3\033[m -> TESOURA {}'''.format(emoji_pedra, emoji_papel, emoji_tesoura))
jogada = int(input('\033[31m->\033[m '))
jogada -= 1
jogadabot = randint(0, 2)
mao = ("PEDRA", "PAPEL", 'TESOURA')
emoji_mao = (emoji_pedra, emoji_papel, emoji_tesoura)
print('jó', end='')
sleep(0.5)
print('ken', end='')
sleep(0.5)
print('pô!')

# se a jogada for invalida, o jogo acaba
exit() if 2 < jogada or jogada < 0 else print('-' * 25)

# verifica as jogadas e mostra o resultado
print('Python   -   Você')
print('-' * 25)
print('{}  x  {} '.format(mao[jogadabot], mao[jogada]))
print('  {}         {}  '.format(emoji_mao[jogadabot], emoji_mao[jogada]))
if jogadabot == jogada:
    print('\033[30m{:^15}\033[m'.format('EMPATE!'))
if jogadabot == 0:
    if jogada == 1:
        print('Você \033[33mGANHOU!\033[m')
    if jogada == 2:
        print('Você \033[31mPERDEU!\033[m')
if jogadabot == 1:
    if jogada == 2:
        print('Você \033[33mGANHOU!\033[m')
    if jogada == 0:
        print('Você \033[31mPERDEU!\033[m')
if jogadabot == 2:
    if jogada == 0:
        print('Você \033[33mGANHOU!\033[m')
    if jogada == 1:
        print('Você \033[31mPERDEU!\033[m')
