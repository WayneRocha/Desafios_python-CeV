# ler 7 valores numericos e colocar em uma lista, duas listas(pares e impares)
# No final mostrar essas listas em ordem crescente

nums = [[], []]     # Pares e impares, respectivamente
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º Número: '))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)
print('=' * 30)
print(f'Números pares: {sorted(nums[0])}')
print(f'Números impares: {sorted(nums[1])}')
