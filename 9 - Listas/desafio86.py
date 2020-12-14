# Ler valores preenchendo uma matriz(3x3). e no final mostrar a matriz formatada

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Matriz 3x3
for c1 in range(0, 3):
    for c2 in range(0, 3):
        matriz[c1][c2] = int(input(f'Digite um valor[{c1 + 1}, {c2 + 1}]: '))
for c1 in range(0, 3):
    for c2 in range(0, 3):
        print(f'{matriz[c1][c2]:^5}', end='')
    print()
