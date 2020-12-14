"""Ler...
- nome do jogador
- quantas partidas ele jogou
- quantidade de gols em cada partida
- total de gols
e guardar tudo num dicionario"""

jogador = dict()
gols = []
jogador['Nome do jogador'] = str(input('Nome do jogador: ')).strip().title()
while True:
    partidas = int(input(f"Quantas partidas o {jogador['Nome do jogador']} jogou?: "))
    if partidas > 0:
        break
print('-' * 43)
for c in range(partidas):
    gols.append(int(input(f'Quantos gols foram feitos na {c + 1}ª partida: ')))
jogador['Gols'] = gols.copy()
jogador['Total de gols'] = sum(jogador['Gols'])
del gols
print('=' * 43)
print(f'{" DADOS ":^43}')
print('=' * 43)
for key, dado in jogador.items():
    if key in 'Gols':
        print(f'{key}:')
        for partida, gol in enumerate(dado):
            print(f'    {partida + 1}ªPartida -> {gol}')
    else:
        print(f'{key:.<20}{dado}')
