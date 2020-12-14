# A função sorteia() sorteia 5 numeros e joga em uma lista

def sorteia():
    from random import sample
    return sample(range(0, 10), 5)


def somaPar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma


nums = sorteia()
print(f'Numeros sorteados {nums}')
print(f'Soma dos valores pares: {somaPar(nums)}')
