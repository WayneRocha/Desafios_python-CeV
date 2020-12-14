# calcular a soma entre todos os números impares que são multiplos de 3 e estejam entre 1 e 500

soma = 0
for c in range(1, 500, 2):
    if c % 2 != 0 and c % 3 == 0 and 1 < c <= 500:
        soma += c
print(f'A soma entre todos os números impares, multriplos de 3 e que estejam entre 1 e 500 é \033[31m{soma}\033[m')
