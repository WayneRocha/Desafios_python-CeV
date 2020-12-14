# ler um número e mostrar o seu fatorial

n = int(input('Digite um número: '))
cont = n
fat = 1
while not cont == 0:
    fat *= cont
    print(cont, end=' x ') if cont != 1 else print(cont, end=' = ')
    cont -= 1
print(fat)
