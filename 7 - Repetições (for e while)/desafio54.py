# ler o ano de nascimento de 7 pessoas. Mostra quantas pessoas atingiram a maior idade(21 anos)

from datetime import date
maior_idade = 0
for c in range(0, 7):
    ano_nasc = int(input('Qual seu ano de nascimento: '))
    if date.today().year - ano_nasc >= 21:
        maior_idade += 1
print(f'Tem {maior_idade} pessoas maiores de idade e')
print(f'{7 - maior_idade} pessoas menores')
