# Cadastrar quantos valores a pessoa quiser e jogalos numa lista
# caso o numero já exista dentro dele, não será adicionado
# Mostra os valores únicos em ordem crescente

numeros = []
while True:
    while True:
        n = int(input('Digite um número: '))
        if len(numeros) == 0:
            numeros.append(n)
            break
        elif n not in numeros:
            numeros.append(n)
            break
        else:
            print('\033[31mDigite um número diferente\033[m\n')
    while True:
        continuar = str(input('Quer \033[4mcontinuar?\033[m: ')).strip().lower()[0]
        if continuar in 'sn':
            break
    if continuar in 'n':
        break
    print('=' * 30)
numeros.sort()
print(f'Os números digitados em ordem crescente ficam:', *numeros, sep=', ')
