# ler quantos Km a pessoa vai viajar e cobrar 0,50 para viagems até 200km e 0,45 para maiores que isso

print("Calcule os custos de sua viagem")
print("-" * 30)
km = float(input("Quantos Km's tem sua viagem? "))
print("-" * 30)
if km <= 200:
    print('Sua viagem vai custar \033[32m{}R$\033[m'.format(km * 0.50))
else:
    print('Sua viagem vai custar \033[32m{}R$\033[m'.format(km * 0.45))
