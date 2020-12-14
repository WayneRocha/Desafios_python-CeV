# ler um número inteiro e dar opções de bases númericas para converter

print('\033[31m==========conversor de bases===========\033[m')
numero = int(input('Digite um número: '))
print('converter para qual \033[30mbase\033[m?')
print('[1] Binario')
print('[2] Octal')
print('[3] Hexadecimal')
base = int(input('-> '))
if base == 1:
    print(f"{numero} convertido para binario é\n{bin(numero)}")
elif base == 2:
    print(f"{numero} convertido para octal é\n{oct(numero)}")
elif base == 3:
    print(f"{numero} convertido para hexadecimal é\n{hex(numero)}")
else:
    print('não foi informado nenhuma das bases acima')
