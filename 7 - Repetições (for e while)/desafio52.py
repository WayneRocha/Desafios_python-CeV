#ler um número inteiro e dizer se ele é ou não PRIMO # como resolver isso???

num = int(input('Digite um número inteiro: '))
primos = 0
for c in range(1, num + 1):
    if num % c == 0:
        primos += 1
if primos == 2:
    print(f'{num} é um número primo')
else:
    print(f'{num} não é um número primo')
