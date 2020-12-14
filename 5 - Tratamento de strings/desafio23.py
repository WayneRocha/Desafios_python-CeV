# ler um número de 0 a 9999 e mostrar da sua únidade ao seu milhar

n = int(input('Digite um número de \033[1m1 a 9999\033[m: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('¨' * 30)
print('unidade: {} '.format(u))
print('Dezena:  {} '.format(d))
print('Centena: {}'.format(c))
print('Milhar:  {}'.format(m))
print('¨' * 30)
