# ler um número e mostrar seu sucessor e antecesor

n = int(input('Digite um número: '))
print('=' * 20)
print('sucessor: {}{}{} \nantessesor: {}{}{}'.format('\033[31m', n+1, '\033[m', '\033[31m', n-1, '\033[m'))
