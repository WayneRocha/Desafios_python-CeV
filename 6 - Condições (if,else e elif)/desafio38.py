# ler dois números, e mostrar se o 1º ou o 2º valor é o maior, ou se os dois são iguais

n1 = float(input('digite um número: '))
n2 = float(input('digito outro número: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 == n2:
    print('Os dois números são iguais')
else:
    print(f'{n2} é maior que {n1}')
