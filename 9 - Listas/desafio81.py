# Ler vários números e colocar numa lista e mostrar...
# quantos numeros foram digitados | Lista em ordem decrescente | Se o 5 está ou não na lista

numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    while True:
        continuar = str(input('Continuar com mais números?: ')).strip().lower()[0]
        if continuar in 'sn':
            break
    if continuar in 'n':
        break
    print('=' * 30)
print('=-' * 30)
print(f'Foram digitados {len(numeros)} números.')
print(f'Números em ordem decrescente: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('O número 5 está na lista de números')
else:
    print('O número 5 não está na lista de números')
