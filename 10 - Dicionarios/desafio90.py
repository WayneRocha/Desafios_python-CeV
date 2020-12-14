# Ler o nome e a media de um aluno e guardar a situação dele num dicionario. No final mostrar  todos os dados

aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip().capitalize()
aluno['Media'] = int(input('Média: '))
if aluno['Media'] < 5:
    aluno['Situação'] = 'Reprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'
print(f'{" DADOS ":=^30}')
for key, val in aluno.items():
    print(f'{key:<9} {val:}')
