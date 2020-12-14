# ler um número e mostrar o seu fatorial

from math import factorial

n = int(input('\033[1mDigite um número\33[m para saber seu fatorial: '))
while n < 1:
    n = int(input('\033[31mInválido\033[m\nDigite um número para saber seu fatorial: '))
print(f'\n\033[4:33m{n}! = {factorial(n)}\033[m')
