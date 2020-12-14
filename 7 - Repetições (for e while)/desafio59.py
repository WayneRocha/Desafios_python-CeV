# ler dois números, e mostrar um menu dando as opções...
# de somar, multiplicar, maior número, novos números, sair do programa

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('-' * 20)
menu = """
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] número maior
[ 4 ] novos números
[ 5 ] sair do programa
"""
print(menu)
escolha = int(input('\033[31m- > \033[m'))
while escolha != 5:
    if escolha == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif escolha == 2:
        print(f'{n1} vezes {n2} é igual a {n1 * n2}')
    elif escolha == 3:
        print(f'entre {n1} e {n2}, o maior número é ', end='')
        print(n1) if n1 > n2 else print(n2)
    elif escolha == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    print('-' * 20)
    print(menu)
    escolha = int(input('\033[31m- > \033[m'))
