# ler o peso de cinco pessoas. no final, mostrar qual foi o maior e o menor peso

maior_peso = 0
menor_peso = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if peso > maior_peso:
        maior_peso = peso
        if menor_peso == 0:
            menor_peso = maior_peso
    if peso <= menor_peso:
        menor_peso = peso
print('-' * 19)
print(f'O maior peso é {maior_peso}Kg\nO menor peso é {menor_peso}Kg')
