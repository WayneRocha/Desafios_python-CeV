# ler vários números inteiros, e o programa para assim que digitar a condição de parada(999)
# no final mostrar quantos números foram digitados, e a soma entre todos os números
# usando o comando break

qt_n = soma = 0
print('\033[1:31m999 -> PARAR\033[m\n')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    qt_n += 1
    soma += n
print('==' * 10)
print(f'\033[1:34m{qt_n} Números fornecidos\nA soma entre todos é {soma}\033[m')
