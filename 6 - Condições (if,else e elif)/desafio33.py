# ler três números e mostrar qual é o maior e qual é o menor

print("Maior e Menor Número")
print("-" * 30)
n1 = float(input('Digite o 1ºNúmero: '))
n2 = float(input('Digite o 2ºNúmero: '))
n3 = float(input('Digite o 3ºNúmero: '))
print("-" * 30)
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
menor = maior
if n1 < menor:
    menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'\033[1mO maior número é {maior:.0f}')
print(f'O menor número é {menor:.0f}\033[m')
