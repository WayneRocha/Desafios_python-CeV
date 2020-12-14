# ler um ano e mostrar se ele é BISEXTO

print("Ano Bisexto?")
print("-" * 20)
ano = int(input('Digite um ano: '))
if ano % 100 != 0 and ano % 4 == 0:
    print('É um ano \033[35mBISEXTO!\033[m')
if ano % 100 == 0 and ano % 400 == 0:
    print('É um ano \033[35mBISEXTO!\033[m')
else:
    print('Apenas um ano normal')
