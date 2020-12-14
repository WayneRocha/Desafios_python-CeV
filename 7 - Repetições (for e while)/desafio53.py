# ler uma frase qualquer, e dizer se ela é um PALINDROMO

frase = str(input('Digite qualquer coisa: '))
palindromo = frase.strip().upper().split()
palindromo = ''.join(frase)
print(f'{frase} ao contrario fica {frase[::-1]}')
if palindromo == palindromo[::-1]:
    print(f'\033[34misso é um palindromo\033[m')
else:
    print(f'\033[31mnão é um palindromo\033[m')
