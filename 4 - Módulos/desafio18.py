# ler o valor de um angulo e mostrar seu seno, cosseno, e a tangente
import math

a = float(input('Digite um \033[7:30mângulo\033[m: '))
a = math.radians(a)
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(math.sin(a), math.cos(a), math.tan(a)))
