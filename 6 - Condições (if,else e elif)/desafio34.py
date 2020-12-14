# ler o salario de um funcionario
# e dar um aumento de 10% para salarios superiores a 1,250,00
# e de 15% para menores ou iguais a 1,250,00

print("Sistema de aumento para funcionários")
print('=' * 40)
salario = float(input('Qual o seu salário? R$'))
print('=' * 40)
if salario > 1250:
    print('PARABÉNS! você receberá um aumento de 10%!')
    print('Seu salario será de \033[32m{}R$\033[m'.format(salario + (salario * 10 / 100)))
else:
    print('PARABÉNS! você receberá um aumento de 15%!')
    print('Seu salario será de \033[32m{}R$\033[m'.format(salario + (salario * 15 / 100)))
