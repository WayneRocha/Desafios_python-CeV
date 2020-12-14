# fazer o computador "pensar" em um número entre 0 e 5
# pedir para o úsuario digitar um número e mostrar se ganhou ou perdeu

from random import randint

na = randint(1, 5)
print('humm, estou pensando em um número, de \033[1m1 a 5\033[m')
n = int(input('Em que número estou pensando? \033[31m->\033[m '))
if na == n:
    print('É esse mesmo! ')
else:
    print(f'Errou! eu tinha pensado {na}')
