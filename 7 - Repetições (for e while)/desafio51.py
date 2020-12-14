# ler o PRIMEIRO TERMO e a RAZÃO de uma PA(progressão aritmética)
# no final mostrar os 10 primeiros termos dessa progressão

pri = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
for c in range(pri, pri + 10 * raz, raz):
    print(c, end=' | ')
print('Fim da progressão')
