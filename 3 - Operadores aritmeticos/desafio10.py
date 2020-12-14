# ler quantos reais ela tem na carteira, e mostrar quantos dólares ela pode comprar

carteira = float(input('Quanto tem na carteira? R$'))
dolar = 5.35    # no dia 1 de junho
dolares = carteira / dolar
print('-' * 30)
print('Você pode comprar até \033[32m${:.2f}\033[m dolares'.format(dolares))
