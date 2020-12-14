"""valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")
"""

# Simular um caixa eletronico --- Perguntar o valor a ser sacado(int)
# o programa vai informar quantas cedulas de cada valor serão dadas

while True:
    notas200 = notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = 0

    print('\033[33m=' * 30)
    print(f'{"Banco PYTHON":^30}')
    print('=' * 30, '\033[m')
    while True:     # série de verificações como, Não impedir o saque de notas de 1 e 3 e de valores não multiplos.
        val = int(input('\033[4:1mQuanto quer sacar? \033[32mR$\033[m'))
        val_uni = int(str(val)[len(str(val)) - 1])  # obtem apenas a unidade do valor
        if val == 1 or val == 3:  # Impedir saque de cédulas de 1 e 3
            print('\033[31mDigite um outro valor\033[m')
            print('=' * 30)
            print("""Cédulas disponiveis:
        R$200 | 20
        R$100 | 10
        R$50  | 5
        R$2""")
            print('=' * 30)
        else:
            if val_uni == (1 or 3 or 6 or 8):
                print('=' * 30)
                print(f'Você pode sacar sacar apenas valores múltiplos!')
                continuar = str(input(f'\033[31mDeseja sacar \033[32mR${val - 1},00\033[m?: ')).strip()[0]
                while continuar not in 'SsNn':
                    continuar = str(input(f'\033[31mDeseja sacar \033[32mR${val - 1},00\033[m?: ')).strip()[0]
                if continuar in 'Ss':
                    break
                print('=' * 30)
            else:
                break
    while True:
        notas200 = val // 200
        val %= 200
        notas100 = val // 100
        val %= 100
        notas50 = val // 50
        val %= 50
        notas20 = val // 20
        val %= 20
        notas10 = val // 10
        val %= 10
        notas5 = val // 5
        val %= 5
        notas2 = val // 2
        val %= 2
        if val == 0:
            break
    print('=' * 30)
    print('\033[32mCédulas\033[m')
    print(f'\033[32m{notas200} de R$200,00\033[m') if notas200 > 0 else print(end='')
    print(f'\033[32m{notas100} de R$100,00\033[m') if notas100 > 0 else print(end='')
    print(f'\033[32m{notas50} de R$50,00\033[m') if notas50 > 0 else print(end='')
    print(f'\033[32m{notas20} de R$20,00\033[m') if notas20 > 0 else print(end='')
    print(f'\033[32m{notas10} de R$10,00\033[m') if notas10 > 0 else print(end='')
    print(f'\033[32m{notas5} de R$5,00\033[m') if notas5 > 0 else print(end='')
    print(f'\033[32m{notas2} de R$2,00\033[m') if notas2 > 0 else print(end='')
    print('=' * 30)
    while True:
        continuar = str(input('Quer fazer mais um saque?: ')).strip()[0]
        if continuar in 'sSnN':
            break
    if continuar in 'Nn':
        break
print('\033[1:33mMuito obrigado! Volte sempre!\033[m')
