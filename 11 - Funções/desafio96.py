# calcular uma areá por meio de uma função

def area(base, altura):
    return base * altura


b = float(input('Base: '))
a = float(input('Altura: '))
print('-' * 10)
print(f'Area: {area(b, a)}')
