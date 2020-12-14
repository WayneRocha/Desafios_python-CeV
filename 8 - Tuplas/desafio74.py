# Gerar 5 numeros aleatórios e colocalos dentro de uma tupla e mostra-la
# mostrar também qual é o menor número e o maior número da tupla

from random import sample
from time import sleep

while True:
    aleatorios = tuple(sample(range(1, 10), 5))
    print(f'Numeros aleatórios: {aleatorios}')
    print(f'Menor número: {min(aleatorios)}\nMaior número: {max(aleatorios)}')
    sleep(5)
    print('\n\n\n')
