# Programa em que o usuario possa ultilizar o interactive help do python. com cores.

def titulo(msg, linha='-', ct=37, stilo=0):
    """
        -> Imprime um titulo personalizado entre 2 linha paralelas.
    :param msg: texto a aparecer no titulo
    :param linha:(opcional) define de qual caractere será formada as linhas
    :param ct:(opcional) Cor do texto, de acordo com os Códigos de cores ANSI (30 a 37)
    :param stilo:(opcional) estilo do texto.
            1 = negrito
            4 = sublinhado
            7 = cor invertida
    :return: Sem retorno
    """
    tam_linha = int((len(msg) + ((50 / 100) * len(msg))) / len(linha))
    print(f'\033[{ct}:{stilo}m', end='')
    print(linha * tam_linha)
    print(f'{msg:^{tam_linha * len(linha)}}')
    print(linha * tam_linha, '\033[m')


def ajuda(comando):
    """
    :param comando: puxa o comando passado do docstring da função help()
    :return: Sem retorno
    """
    if comando == 'fim':
        print('BONS ESTUDOS!')
        exit()
    else:
        titulo(f'Módulo {comando}', '~', 33, 1)
        print('\033[1m', end='')
        help(comando)
        print('\033[m', end='')


while True:
    print('=' * 25)
    ajuda(str(input('\033[7:30mComando ou Biblioteca: \033[m')))
