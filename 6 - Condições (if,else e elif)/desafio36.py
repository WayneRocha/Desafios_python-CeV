# aprovar um emprestimo bancario para a compra de uma casa.
# o programa coleta o | valor da casa | salario do comprador | quantos anos ele vai pagar
# calcula  o valor da prestação mensal
# o valor dessa prestação não pode exceder 30% do salario

print('============EMPRESTIMOS BANCARIOS PARA CASAS===========')
nome = str(input('Ola! Qual seu nome? ')).strip().split()
vcasa = float(input('Qual o valor da casa? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
salario = float(input('Qual o valor do seu salário[mensal]? R$'))
print('=-' * 25)
emprestimo = vcasa / (anos * 12)
if emprestimo <= salario * 30 / 100:
    print(f"\033[1mSeu emprestimo foi aprovado\033[m, e ficará por R${emprestimo:.2f}/Mês por {anos} Anos")
    print(f'Muito obrigado por fazem negocios conosco {nome[0].capitalize()}! :)')
else:
    print('Infelizmente seu emprestimo não foi aprovado :(')
