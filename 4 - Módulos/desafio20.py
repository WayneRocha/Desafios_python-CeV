# sortear a ordem de apresentação de trabalhos 4 alunos

from random import sample
print('-----Quem apresenta primeiro------')
a1 = str(input('Nome do 1º aluno: '))
a2 = str(input('Nome do 2º aluno: '))
a3 = str(input('Nome do 3º aluno: '))
a4 = str(input('Nome do 4º aluno: '))
sorteio = [a1, a2, a3, a4]
print('-' * 30)
print('\033[1mOs alunos que se apresentarão\033[m \n{}{}{}'.format("\033[35m", sample(sorteio, 4), "\033[m"))
