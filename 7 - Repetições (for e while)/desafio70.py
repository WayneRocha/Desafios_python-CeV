# ler o nome e o preço de vários produtos. Quando terminar de comprar mostrar...
# O total da compra | Quantos produtos custam mais de R$1000,00 | Qual o nome do produto mais barato

total = itens = qt_prod_1000 = prod_barato = nome_prod_mbarato = 0
lista = ''

print('=' * 20)
print(f'{"SHOPPING":^20}')
print('=' * 20)

while True:
    nome = str(input('Produto: ')).capitalize()
    val = float(input('Preço: \033[32mR$\033[m'))
    while val < 0.00:
        val = float(input('Preço: \033[32mR$\033[m'))

    carrinho = str(input('Quer adicionar mais ao carrinho?: '))[0]
    while carrinho not in 'SsNn':
        carrinho = str(input('Quer adicionar mais ao carrinho?: '))[0]

    total += val
    itens += 1
    lista += f'\n[{itens}] {nome}'
    if val > 1000:
        qt_prod_1000 += 1
    if prod_barato == 0:
        prod_barato = val
    else:
        if val < prod_barato:
            prod_barato = val
            nome_prod_mbarato = nome

    print('=' * 20)
    if carrinho in 'Nn':
        break

print('=' * 20)
print(f'Lista de compras\n{lista}')
print('=' * 20)
print(f'Total: \033[1:32mR${total:.2f}\033[m')
if qt_prod_1000 > 0:
    print(f'\033[1:32m{qt_prod_1000}\033[m Produtos custam \033[1:32m+ de R$1000,00\033[m')
if nome_prod_mbarato != 0:
    print(f'O \033[1:32m{nome_prod_mbarato}\033[m é o produto \033[1:32mmais barato\033[m')
