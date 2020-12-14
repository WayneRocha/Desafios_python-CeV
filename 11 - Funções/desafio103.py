# função calcula o aproveitamento deo jogador, o programa deve mostrar uma ficha do jogador

def ficha(nome='<desconhecido>', gols=0):
    """
    :param nome: Nome do jogador
    :param gols: quantidade de gols
    :return: retorna a frase "O jogador ... fez ... gol(s) no campeonato"
    """
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


print(ficha(gols=0))
