# Ler números perguntando se o úsuario quer continuar
# No final, mostrar a média entre todos os números e qual é o maior e qual é o menor

continuar = 'S'
cont = media = 0
while 'S' in continuar:
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar?: ')).upper()
    cont += 1
    media += n
    if cont == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    print('\n', '-=' * 20, '\n')
media = media / cont
print(f'Média: {media:.2f}\nMaior números: {maior}\nMenor número: {menor}')
