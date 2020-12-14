# funcao que receba 3 parametros(inicio, fim e passo)
# programa deve contar de 1 a 10 de 1 em 1, e depois de 10 a 0 de 2 em 2
# no final uma contagem personalizada

from time import sleep


def contagem(inicio, fim, passo=1):
    if passo == 0:
        passo = 1
    if inicio > fim:
        if passo > 0:
            passo *= -1
        fim -= 1
    else:
        if passo < 0:
            passo = abs(passo)
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' ', flush=True)
        sleep(abs(.1 / ((3 / 100) * (inicio + fim))))
    print()


print('-' * 20)
contagem(1, 10)
print('-' * 20)
contagem(10, 0, 2)
print('-' * 20)
print(f'{" SUA CONTAGEM ":=^20}')
while True:
    i = int(input('Inicio: '))
    f = int(input('Fim: '))
    if i != f:
        break
    else:
        print(f'\033[31mVocê  não pode contar de {i} até {f}!\033[m')
p = int(input('Passo: '))
print('=' * 20)
contagem(i, f, p)
