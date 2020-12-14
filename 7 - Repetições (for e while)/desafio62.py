# melhorar o desafio 61, perguntando para o úsuario mais quantos termos ele quer ver

pt = int(input('Digite o primero termo: '))
raz = int(input('digite a razão: '))
term = prog = 0
maisterm = 1
print('10 Primeiros termos da PA\n\033[33m')
while maisterm != 0:
    while term < 10 + maisterm:
        prog = pt + raz * term
        print('\033[33m', prog, end=' | \033[m')
        term += 1
    maisterm = int(input('\n\033[mQuantos termos da PA ainda deseja ver?: \033[m'))
    term = 0
print('\n\n\033[mFim da prograssão')
