# ler  um valor em metros, e mostra-lo em centimetros e milimetros

val = float(input('digite um valor em metros: '))
print('=' * 25)
print('\033[1:30mcentrimetros: {}'.format(val * 100))
print('milimetros:   {}\033[m'.format(val * 1000))
