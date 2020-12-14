# ler um número e mostrar abaixo sua tabuada

f = {'fundoI': '\033[1:46m',
     'fundoF': '\033[m'}
val = int(input('Digite um número: '))
print('===TABUADA===')
print('{}{} X {}  = {}{}'.format(f['fundoI'], val, 1, val * 1, f['fundoF']))
print('{}{} X {}  = {}{}'.format(f['fundoI'], val, 2, val * 2, f['fundoF']))
print('{}{} X {}  = {}{}'.format(f['fundoI'], val, 3, val * 3, f['fundoF']))
print('{}{} X {}  = {}{}'.format(f['fundoI'], val, 4, val * 4, f['fundoF']))
print('{}{} X {}  = {}{}'.format(f['fundoI'], val, 5, val * 5, f['fundoF']))
print('{}{} X {}  = {}{}'.format(f['fundoI'], val, 6, val * 6, f['fundoF']))
print('{}{} X {}  = {}{}'.format(f['fundoI'], val, 7, val * 7, f['fundoF']))
print('{}{} X {}  = {}{}'.format(f['fundoI'], val, 8, val * 8, f['fundoF']))
print('{}{} X {}  = {}{}'.format(f['fundoI'], val, 9, val * 9, f['fundoF']))
print('{}{} X {} = {}{}'.format(f['fundoI'], val, 10, val * 10, f['fundoF']))
print('=' * 14)
