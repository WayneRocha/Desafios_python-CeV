# Uma função que calcule o fatorial.
# de acordo com um parametro logico, mostrar ou não o processo de calculo do fatorial


def fatorial(n, show=False):
    """
    -> Mostra o fatorial de um número
    :param n: Número a ser calculado o fatorial
    :param show: (opcional)Retorna uma string com o processo do fatorial
                 Ex: "5 x 4 x 3 x 2 x 1 = 120"
    :return: retorna o fatorial do parametro "n", caso o parametro "show" seja True, a função retorna
             uma string com o processo do fatorial
    """
    fat = 1
    if show:
        processo = ''
        for c in range(n, 0, -1):
            fat *= c
            if c == 1:
                processo += f'{c} = {fat}'
            else:
                processo += f'{c} x '
        return processo
    else:
        for c in range(n, 1, -1):
            fat *= c
        return fat


print(fatorial(5, True))
