# ler nome, sexo e idade de várias pessoas. mostrar...
# Quantas pessoas foram cadastradas ✔
# A média de idade do grupo 
# Lista com todas as mulheres ✔
# Lista de pessoas acima da média

l_pessoas = list()
l_mulheres = list()
l_pessoasAcimadaMedia = list()
dados_pessoa = dict()
while True:
    dados_pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados_pessoa['idade'] = int(input('Idade: '))
        if dados_pessoa['idade'] > 0:
            break
    while True:
        dados_pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if dados_pessoa['sexo'] in 'MF':
            break
    while True:
        continuar = str(input('Continuar?: ')).strip()[0]
        if continuar in 'SsNn':
            break
    l_pessoas.append(dados_pessoa)
    if continuar in 'Nn':
        break
qtn_cadastros = len(l_pessoas)
soma_media = 0
for pessoa in l_pessoas:
    soma_media += pessoa['idade']
media_idade = soma_media / len(l_pessoas)
del soma_media
for pessoa in l_pessoas:
    if pessoa['sexo'] == 'F':
        l_mulheres.append(pessoa)
    if pessoa['idade'] > media_idade:
        l_pessoasAcimadaMedia.append(pessoa)
print(media_idade)
print(qtn_cadastros)
print(l_mulheres)
print(l_pessoasAcimadaMedia)
