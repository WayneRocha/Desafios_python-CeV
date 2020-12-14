# ajudar o professor a sortear um aluno para apagar a lousa no final da aula
# ler o nome dos 4 alunos e mostrar sortear qual apagará a lousa

from random import choice
print('------sorteador de alunos------')
a1 = str(input('Nome do 1º aluno: '))
a2 = str(input('Nome do 2º aluno: '))
a3 = str(input('Nome do 3º aluno: '))
a4 = str(input('Nome do 4º aluno: '))
sorteio = [a1, a2, a3, a4]
print('-' * 30)
print('Sorteado o aluno {}{}{}'.format("\033[1:4m", choice(sorteio), "\033[m"))
