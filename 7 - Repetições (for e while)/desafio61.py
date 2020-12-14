# ler o primeiro termo e a razão de uma PA(progressão aritmética) e mostrar os 10 primeiros termos

pt = int(input('Digite o primero termo: '))
raz = int(input('digite a razão: '))
term = 0
print('10 Primeiros termos da PA\n\033[33m')
while term < 10:
    print(pt + raz * term, end=' | ')
    term += 1
print('\n\n\033[mFim da prograssão')
