# Fazer o exercicio 9 de tabuada usando a estrutura FOR

tabuada = int(input('Qual tabuada você quer ver? -> '))
for c in range(1, 11):
    print('{} X {} = {}'.format(tabuada, c, tabuada * c))
