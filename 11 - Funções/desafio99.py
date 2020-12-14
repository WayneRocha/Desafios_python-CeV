# uma função recebe vários valores e retorna qual é o maior valor

def maior(valores):
    return max(valores)


from random import sample
from time import sleep
while True:
    lista = sample(range(0, 50), 5)
    print(f'valores passados -> ', end='')
    print(*lista, sep=', ')
    print(f'Maior valor da lista {maior(lista)}')
    sleep(5)
    print('\n\n')
