# ler uma frase e mostrar...
## quantas vezes aparece a letra 'A'
## em que posição aparece pela primeira vez
## em que posição aparece pela última vez

frase = str(input('Digite alguma frase: ')).upper().strip()
print('A letra \033[31m"A"\033[m aparece {} vezes'.format(frase.count('A')))
print('Aparece pela primeira vez na posição {}'.format(frase.find('A') + 1))
print('Aparece pela Última vez na posição {}'.format(frase.rfind('A') + 1))
