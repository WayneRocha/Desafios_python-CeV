# executar o exercicio 35 e caso possa formar um triangulo, mostrar se é...
# Equilatero(todos iguais) | isoceles(dois iguais) | escaleno(todos diferentes)

print('========Triangulator========')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    if r1 == r2 == r3:                      # se todos forem iguais...
        print('É um triangulo Equilatero')
    elif r1 == r2 or r2 == r3 or r1 == r3:  # se dois  forem iguais...
        print('É um triangulo Isoceles')
    elif r3 != r1 != r2 != r3:                    # se todos forem diferentes...
        print('É um triangulo Escaleno')
else:
    print('Não pode formar um triangulo')
