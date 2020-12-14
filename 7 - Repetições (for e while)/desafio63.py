# O úsuario digita quantos termos da sequencia de fibonacci quer ver

n1 = n2 = 0
fib = 1
cont = int(input('Quantos termos da \033[34mSequência de Fibonacci\033[m quer ver?: '))
while cont != 0:
    print(f'\033[34m{fib}\033[m', end=' | ')
    n2 = n1 + fib
    n1 = fib
    fib = n2
    cont -= 1
print('\n\nFim da sequencia')
