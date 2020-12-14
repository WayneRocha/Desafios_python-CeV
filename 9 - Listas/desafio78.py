# Ler 5 numeros pelo teclado  e guardalos numa lista
# Mostrar o maior e menor valor digitados e suas posições na lista
from typing import List

numeros = []
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite o {c + 1}º Número: ')))
print('=' * 30)
minimo = min(numeros)
maximo = max(numeros)
for pos, n in enumerate(numeros):
    if maximo == n:
        maior = [n , pos + 1]
    if minimo == n:
        menor = [n, pos + 1]
print(f'O maior valor da lista é {maior[0]} na posição {maior[1]}')
print(f'O menor valor da lista é {menor[0]} na posição {menor[1]}')
del minimo, maximo
