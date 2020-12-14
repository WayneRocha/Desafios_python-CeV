# Ler um nome completo, e mostrar o 1º e o último nome

nome = str(input('Seu nome completo: ')).strip()
nome = nome.split()
print('Olá \033[4m' + (nome[0] + ' ' + nome[len(nome) - 1]).title())
