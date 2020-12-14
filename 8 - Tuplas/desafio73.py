# de acordo com a tabela do campeonato brasileiro, mostrar
# 5 primeiros colocados | 4 últimos colocados | A tabela em ordem alfabetica | a posição do time do São paulo

brasileirao = ('Atlético-MG', 'Internacional', 'Palmeiras', 'Flamengo', 'Sport Recife', 'Santos', 'São Paulo',
               'Fluminense', 'Vasco da Gama', 'Fortaleza', 'Atlético-GO', 'Athletico-PR', 'Ceará SC', 'Corinthians',
               'Grêmio', 'Bahia', 'Coritiba', 'Bragantino-SP', 'Botafogo', 'Goiás')
print('-' * 20)
print(f"\033[1:32m{'Brasileirão Serie A':^20}\033[m")
print('-' * 20)
for pos, time in enumerate(brasileirao):
    print(f'{pos + 1}º{time:^20}')
print('-' * 20)
print(f'\033[1:32m{"informações":^110}\033[m')
print(f"""\033[32m
\033[1:32m5 Primeiros colocados ->\033[m {brasileirao[0:5]}

\033[1:32m4 Ùltimos colocados ->\033[m {brasileirao[-4:]}

\033[1:32mTabela em ordem alfabética ->\033[m {sorted(brasileirao)}

São paulo está na \033[1:32m{brasileirao.index("São Paulo") + 1}ªposição\033[m

""")
