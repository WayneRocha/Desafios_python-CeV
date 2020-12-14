# Ler 5 valores numericos e mostralos em ordem crescente sem o sort()

numeros = []
suc = [0, 0]    # Número e posição respectivamente
ant = [0, 0]    # Número e posição respectivamente
for i in range(0, 5):
    n = int(input(f'Digite o {i + 1}º Número: '))
    if len(numeros) == 0:
        numeros.append(n)
        print('Primeiro número adicionado a lista')
    elif n >= max(numeros):
        numeros.append(n)
        print('Número adicionado ao final da lista')
    elif n <= min(numeros):
        numeros.insert(0, n)
        print('Número adicionado ao começo da lista')
    else:
        for pos, num in enumerate(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                suc = [numeros[pos + 1], pos + 1]
                ant = [numeros[pos - 1], pos - 1]
                break
        print(f'Número adicionado entre os numeros {ant[0]} e {suc[0]}')
    print('=' * 35)
print(f'O números digitados foram: {numeros}')
