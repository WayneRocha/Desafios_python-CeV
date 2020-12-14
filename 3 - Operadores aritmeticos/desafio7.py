# ler duas notas de um aluno e mostrar a média do aluno

print('\033[30m=========\033[m \033[31mETEC ZL\033[m \033[30m=========\033[m')
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2
print('\033[1mMédia do aluno é \033[1:32m{}\033[m\033[m'.format(media))
