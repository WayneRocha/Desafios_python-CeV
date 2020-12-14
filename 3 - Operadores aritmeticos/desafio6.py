# ler um número e mostrar o seu dobro, triplo e raiz quadrada

n = int(input('Digite um Número: '))
dobro = n * 2
triplo = n * 3
raizQ = n**(1/2)
print('=' * 20)
print('Dobro:{:>20} \nTriplo:{:>20} \nRaiz Quadrada:{:>20}'.format(dobro, triplo, raizQ))
