# Ler vários números e colocalos numa lista e no final...
# mostrar a lista original e 2 listas, uma com os números pares e a outra com os impares da lista original

numeros = []
numerosP = []
numerosI = []

while True:
    numeros.append(int(input('Digite um número: ')))
    while True:
        continuar = str(input('Quer adicionar mais numeros? ')).strip().lower()[0]
        if continuar in 'sn':
            break
    if continuar in 'n':
        break
    print('=' * 30)
print('=-' * 30)
for n in numeros:
    if n % 2 == 0:
        numerosP.append(n)
    else:
        numerosI.append(n)
print(f'Números digitados: {numeros}')
if len(numerosP) > 0:
    print(f'Números pares: {numerosP}')
if len(numerosI) > 0:
    print(f'Números impares: {numerosI}')
