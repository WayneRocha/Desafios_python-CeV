# calcular o valor a ser pago por um produto considerando o preço e a condição de pagamento
# a vista no dinheiro/cheque(10% de desconto) | a vista no cartao(5%)
# até 2x no cartão(preço normal) | 3x no cartão(20% de juros)

print('Olá! :D')
print('Seja muito bem vindo ao torratorraseudinheiro!')
print('=' * 25)
print('Qual Produto você quer?')
print('-' * 25)
print('''
\033[33m1\033[m - Sapato [R$150,00]
\033[33m2\033[m - Calsa [R$30,00]
\033[33m3\033[m - Terno [R$200,00]
\033[33m4\033[m - Terno + camisa [R$250,00]
\033[33m5\033[m - vestido [R$150,00]''')
roupa = int(input('-> '))
if roupa == 1:
    preco = 150
elif roupa == 2:
    preco = 30
elif roupa == 3:
    preco = 200
elif roupa == 4:
    preco = 250
elif roupa == 5:
    preco = 150
else:
    print('Nenhum produto foi escolhido')
    print('Volte sempre!')
    exit()
print('-' * 25)
print('Como gostaria de pagar?')
print('-' * 25)
print('''
\033[33m1\033[m - A vista no dinheiro/cheque
\033[33m2\033[m - A vista no cartao(5%)
\033[33m3\033[m - 2x no cartão
\033[33m4\033[m - 3x no cartão''')
pag = int(input('-> '))
print('-' * 25)
if pag == 1:
    desconto = 10
    pagar = preco - (preco * desconto / 100)
    print(f'O total fica R${pagar},00 com {desconto}% de deconto')
    print('muito obrigado por gastar seu dinheiro conosco :)\nVolte sempre!')
elif pag == 2:
    desconto = 5
    pagar = preco - (preco * desconto / 100)
    print(f'O total fica R${pagar},00 com {desconto}% de deconto')
    print('muito obrigado por gastar seu dinheiro conosco :)\nVolte sempre!')
elif pag == 3:
    pagar = preco
    print(f'O total fica R${pagar},00 parcelado[2x]')
    print('muito obrigado por gastar seu dinheiro conosco :)\nVolte sempre!')
elif pag == 4:
    juros = 20
    pagar = (preco + (preco * juros / 100)) / 3
    print(f'O total fica R${pagar},00/mês parcelado[3x] com {juros}% de juros')
    print('muito obrigado por gastar seu dinheiro conosco :)\nVolte sempre!')
else:
    print('Nenhuma forma de pagamento foi escolhida')
    print('Volte sempre!')
