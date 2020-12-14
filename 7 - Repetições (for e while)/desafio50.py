# ler seis números inteiros e mostrar a soma dos que forem PARES

soma = 0
for c in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
print(f'A soma de todos os números pares é \033[31m{soma}\033[m')
