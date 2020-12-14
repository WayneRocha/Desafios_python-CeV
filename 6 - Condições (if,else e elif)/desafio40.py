# ler duas notas de um aluno e calcular sua média
# de acordo com a média, mostrar se o aluno está...
# reprovado(abaixo de 5) | de recuperação(entre 5 e 6,9) | aprovado(acima de 7)

nota1 = float(input('1ªnota do aluno: '))
nota2 = float(input('2ªnota do aluno: '))
media = (nota1 + nota2) / 2
print('-' * 10)
if media < 5:
    print('Aluno \033[1:31mreprovado\033[m')
elif 5 <= media < 7:    # maior ou igual 5 e menor que 7
    print('Aluno de \033[31mrecuperação\033[m')
else:
    print('Aluno \033[34maprovado\033[m')
