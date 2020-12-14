# ler em uma tupla as vogais de cada palavra e mostra-las na tela

palavras = ('frutos do espirito', 'amor', 'alegria', 'paz', 'paciencia', 'bondade', 'benignidade', 'fe')
print('\033[34m', end='')
print('=' * 66)
print(f'\033[1m{"Palavras e suas vogais":^66}\033[34m')
print('=' * 66, '\033[m')
for word in palavras:
    print(f'\nPalavra: \033[34m{word:<18}\033[m | Vogais: \033[34m', end='')
    for letra in word:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' | ')
    print('\033[m', end='')
