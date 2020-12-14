# ler o nome de uma pessoa e mostrar...
# em maiusculas e minusculas
# quantas letras o nome inteiro tem ,sem espaços
# e quantas letras tem o primeiro nome

corlinha = {'LI': '\033[1:30m', 'LF': '\033[m'}
nome = str(input('Qual seu nome? ')).strip()
print(f"{corlinha['LI']}¨{corlinha['LF']}" * 40)
print('Maiusculo:', nome.upper())
print(f"{corlinha['LI']}¨{corlinha['LF']}" * 40)
print('Minusculo:', nome.lower())
print(f"{corlinha['LI']}¨{corlinha['LF']}" * 40)
print('Número de letras:', len(nome) - nome.count(' '))
print(f"{corlinha['LI']}¨{corlinha['LF']}" * 40)
nome = nome.split()
print('Número de letras do 1ºnome: ', len(nome[0]))
print(f"{corlinha['LI']}¨{corlinha['LF']}" * 40)
