# ler quatro valores e colocalos em uma tupla, no final mostrar...
# Quantas vezes aparecem o valor 9 | Em que posição foi digitado o 1º valor 3 | Quais números são pares


numeros = (int(input('Digite o 1º valor: ')),
           int(input('Digite o 2º valor: ')),
           int(input('Digite o 3º valor: ')),
           int(input('Digite o 4º valor: ')))
vezes9 = numeros.count(9)
pares = ''
position3 = -1
for pos, n in enumerate(numeros):
    if n % 2 == 0:
        pares += f"{n}, "
    if n == 3 and position3 == -1:
        position3 = pos + 1
print('=' * 30)
print(f'Numeros digitados: {numeros}\n')
if pares not in '':
    print(f'Os números pares são: {pares[:-2]}')
if position3 > 0:
    print(f'o número 3 aparece primeiro na posição {position3}')
if vezes9 > 0:
    print(f'o número 9 aparece {vezes9} vez', end='')
    print('es') if vezes9 > 1 else print('\n')
