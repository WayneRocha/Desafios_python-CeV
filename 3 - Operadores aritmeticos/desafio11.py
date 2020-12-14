# calcular a área de uma parede a partir da base e da altura fornecidos
# depois mostrar quantos litros de tinta é nescessario para pintar toda a parede
# sendo que cada litro de tinta pinta 2M²
print('====Calculardora para pintores====')
b = float(input('Digite a base: '))
a = float(input('digite a altura: '))
area = a * b
l_tinta = area / 2
print('=' * 20)
print('A parede tem \033[4m{}M²\033[m'.format(area), end=' ')
print('e voce precisa de \033[4m{}Litros de tinta\033[m \npara pintar a parede toda.'.format(l_tinta))
