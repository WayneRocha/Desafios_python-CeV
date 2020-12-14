# Ler o nome e o peso de várias pessoas. guardando-as em uma lista e mostre...
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas(pesado é >= 80)
# Uma listagem com as pessoas mais leves(leve é < 80)

pessoas = [[], []]  # Pessoas pesadas e leves, respectivamente
while True:
    pessoa = str(input('Seu nome: '))
    while True:  # Evitar peso negativo
        peso = float(input('Seu peso: '))
        if peso > 0:
            break
    if peso >= 80:
        pessoas[0].append([pessoa, peso])
    else:
        pessoas[1].append([pessoa, peso])
    while True:     # Verificar se quer continuar
        continuar = str(input('Quer continuar? ')).strip()[0]
        if continuar in 'sSnN':
            break
    if continuar in 'Nn':
        break
    print('\033[32m=\033[m' * 30)
print('=-' * 15)
print(f'Pessoas leves: {pessoas[1]}')
print(f'Pessoas Pesadas: {pessoas[0]}')
