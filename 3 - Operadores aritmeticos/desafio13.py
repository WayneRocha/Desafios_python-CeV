# ler o salario de um funcionario e mostra quanto será com 15% de aumento

print('=====AUMENTO DE SALARIO=====')
salario = float(input('Qual seu salário? '))
aumento = salario + (15 * salario / 100)
print('O salário com \033[1:4:33m15% de aumento\033[m é \033[1:32mR${}\033[m'.format(aumento))
