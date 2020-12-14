# ler vários números inteiros, e o programa para assim que digitar a condição de parada(999)
# no final mostrar quantos números foram digitados, e a soma entre todos os números

CP = cont = soma = 0
print('\033[31mPara parar digite "999"\033[m')
while CP != 999:
    n = int(input('Digite um número: '))
    CP = n
    soma += n
    cont += 1
cont -= 1
soma -= 999
print('-=' * 20)
print(f'foram \033[34mdigitados {cont} números\033[m e a \033[34msoma\033[m entre todos é \033[34m{soma}\033[m')
