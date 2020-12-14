# o computador vai pensar em um número de 0 a 10, o jogador vai tentar advinhar o número
# no final vai mostrar quantos palpites foram nescessarios para acertar

from random import randint

print('Estou pensando em um número de 0 a 10...')
python = randint(1, 10)
jogada = int(input('Qual número estou pensando? -> '))
tentativas = 1
while python != jogada:
    tentativas += 1
    print('-' * 20)
    if python > jogada:
        print('Um pouco mais...')
    else:
        print('Um pouco menos...')
    print('Estou pensando em um número de 0 a 10...')
    jogada = int(input('Qual número estou pensando? -> '))

print('-' * 20)
print('Acertou!')
print('De primeira! Parabéns') if tentativas == 1 else print(f'Você precisou de {tentativas} Tentativas para acertar')