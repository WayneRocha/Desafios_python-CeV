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
        if val == (1 or 3):  # Impedir saque de cédulas de 1 e 3
            print('\033[31mDigite um outro valor\033[m')
            print('=' * 30)
            print("""Cédulas disponiveis:
        R$200 | 20
        R$100 | 10
        R$50  | 5
        R$2""")
            print('=' * 30)
        else:
            if val_uni == (1 or 3):
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
        if val >= 200:
            val -= 200
            notas200 += 1
        elif val >= 100:
            val -= 100
            notas100 += 1
        elif val >= 50:
            val -= 50
            notas50 += 1
        elif val >= 20:
            val -= 20
            notas20 += 1
        elif val >= 10:
            val -= 10
            notas10 += 1
        elif val >= 5:
            val -= 5
            notas5 += 1
        elif val >= 2:
            val -= 2
            notas2 += 1
        # quando o valor tem as unidades 6 e 8, o "val" sempre acaba em 1 e consequentemente em um loop infinito
        # isso acontece porque a nota 5 é contada, mas ao terminar com essas unidades, a contagem das notas muda
        # para mudar o esquema de contagem, pegue a unidade do valor original e faça uma regra especifica para eles
        elif val == 1:
            notas5 = notas2 = 0
            if val_uni == 6:  # se a unidade for 6 ele vai reorganizar as cédulas
                notas2 = 3  # 3 notas de 2 reais = 6 reais
            elif val_uni == 8:  # se a unidade for 8 ele vai reorganizar as cédulas
                notas2 = 4  # 4 notas de 2 reais = 8 reais
            val = 0
        elif val == 0:
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
