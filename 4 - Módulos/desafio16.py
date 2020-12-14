# ler um numero com , qualquer e mostrar o numero inteiro

from math import trunc

n = float(input('Digite um número real(ex:1.1): '))
print(f"Arredondando fica \033[1:31m{trunc(n)}\033[m")
