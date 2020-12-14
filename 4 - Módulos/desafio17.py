# ler o comprimento do cateto oposto e do  cateto adjacente de um triagulo retangulo
# calcular e mostrar o comprimento da hipotenusa
from math import hypot

co = float(input('Comprimento do \033[31mcateto oposto\033[m: '))
ca = float(input('comprimento do \033[31mcateto adjacente\033[m: '))
hip = hypot(co, ca)
print('A \033[4:31mhipotenusa\033[m do triangulo é \033[1:31m{:.1f}\033[m'.format(hip))
