# ler um número e dizer se ele é PAR ou Impar

print("Par ou Impar?")
print("-" * 20)
n = int(input('Digite um número: '))
if n % 2 == 0:
    print('o número é \033[36mPAR!\033[m')
else:
    print('O número é \033[36mIMPAR!\033[m')
