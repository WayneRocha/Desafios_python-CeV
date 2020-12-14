# Fazer o mesmo que o desafio anterior(desafio 86). mas no final mostrar...
# A soma dos numeros pares | A soma dos valores da 3ªcoluna | O maior valor da 2ª linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Matriz 3x3
somaP = soma3 = mai2 = 0
for c1 in range(0, 3):      # preechimento da matriz
    for c2 in range(0, 3):
        matriz[c1][c2] = int(input(f'Digite um valor[{c1 + 1}, {c2 + 1}]: '))
        if matriz[c1][c2] % 2 == 0:     # Verifica se há valor par
            somaP += matriz[c1][c2]
        if c2 == 2:                     # Verifica se está na 3ª coluna e incrementa
            soma3 += matriz[c1][c2]
mai2 = max(matriz[1])       # Obtem o maior valor da 2ªlinha
print(f'\n{"Matriz":^15}')
for c1 in range(0, 3):      # Exibe a matriz
    for c2 in range(0, 3):
        print(f'{matriz[c1][c2]:^5}', end='')
    print()
print()
print(f'A soma dos números pares é {somaP}')
print(f'A soma dos valores da 3ª coluna é {soma3}')
print(f'O maior valor da 2ª linha é {mai2}')
