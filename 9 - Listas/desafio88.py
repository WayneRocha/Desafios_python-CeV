# Criar uma quantidade de Palpites (6 numeros entre 1 e 60(sorteados, sem repetir)). Cadastrar tudo em uma lista

from random import sample
from time import sleep
jogos = []
print('=' * 30)
print(f'\033[1:33m{"Python da sorte":^30}\033[m')
print('=' * 30)
qnt = int(input('Quanto palpites você quer?: '))
for c in range(qnt):
    jogos.append(sample(range(1, 60), 6))
print(f'\033[1:33m{" PALPITES ":=^30}\033[m')
for c, jogo in enumerate(jogos):
    print(f'Jogo {c + 1} - {jogo}')
    sleep(.5)
