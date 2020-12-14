# Pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('=====aluguel de carros=====')
dias = int(input('Quantos \033[1mdias\033[m foi alugado? '))
km = float(input('Quantos \033[1mKm\033[m foram rodados? '))
dia_alg = 60
km_alg = 0.15
preco = (dias * dia_alg) + (km * km_alg)
print(f'O total a pagar é \033[1:32mR${preco:.2f}')
