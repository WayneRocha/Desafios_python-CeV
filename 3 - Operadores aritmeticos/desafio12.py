# ler o preço, e mostrar seu preço com 5% de desconto

preco = float(input('Quanto custa o produto?'))
desconto = preco - (5 * preco / 100)
print('com nossa \033[1:4:33mpromoção de 5%\033[m, o produto fica \033[1:32mR${}\033[m'.format(desconto))
