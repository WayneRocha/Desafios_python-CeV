# ler um número e mostrar o seu fatorial

n = int(input('Digite um número: '))
cont = n
fat = 1
for cont in range(cont, 0, -1):
    fat *= cont
    print(cont, end=' x ') if cont != 1 else print(cont, end=' = ')
print(fat)
