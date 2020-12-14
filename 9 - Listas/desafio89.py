# Ler o nome e duas notas de vários alunos e cadastrar numa lista composta(3 niveis), no final mostrar...
# Um boletim com a média de cada um. E permitir que o usuario escolha ver a nota de cada um, individualmente.

alunos = []
while True:     # Cadastro dos alunos
    nome = str(input('Nome do aluno: ')).strip().capitalize()
    while True:     # impede notas negativas
        nota1 = float(input('Nota do 1º semestre: '))
        nota2 = float(input('Nota do 2º semestre: '))
        if (nota1 or nota2) < 0:
            print('\033[31mNotas invalida!\033[m')
        else:
            media = (nota1 + nota2) / 2     # Calcula a média do aluno
            break
    alunos.append([nome, media, [nota1, nota2]])    # Adiciona os dados a lista, respectivamente
    while True:     # Verifica se quer continuar cadastrando
        continuar = str(input('Cadastrar mais alunos?: ')).strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        del nome, nota1, nota2, continuar, media
        break
    print('\033[1m=\033[m' * 36)
print(f'\033[34m{" BOLETINS ":=^36}\033[m')
print('\033[4mID.   Nome                  Média   \033[m')
for num, aluno in enumerate(alunos):    # Mostra o "ID", o nome e a media em forma de tabela
    print(f'{num + 1:<6}{aluno[0]:<22}{aluno[1]:<8}')
while True:     # Verifica se quer ver mais sobre o aluno e verifica a resposta
    detalhes = str(input('Quer detalhes sobre a nota de um aluno?: ')).strip()[0]
    if detalhes in 'SsNn':
        break
if detalhes in 'Ss':
    while True:
        while True:     # Fornecer o "id" do aluno e ver se é valido
            identificador = int(input('Qual o ID do aluno?: '))
            if identificador in range(1, len(alunos) + 1):
                break
        print('=' * 36)
        print(f'Nome do aluno: {alunos[identificador - 1][0]}')
        print(f'Média: {alunos[identificador - 1][1]}')
        print(f'Nota do 1º semestre: {alunos[identificador - 1][2][0]}')
        print(f'Nota do 2º semestre: {alunos[identificador - 1][2][1]}')
        while True:  # Verifica se quer continuar vendo detalhes
            continuar = str(input('Quer mais detalhes sobre a nota de um aluno?: ')).strip()[0]
            if continuar in 'SsNn':
                break
        if continuar in 'Nn':
            break
