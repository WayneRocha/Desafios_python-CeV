# função que recebe várias notas e retorna um dicionário com...
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação(opicional)

def notas(*n, sit=False):
    """
    :param n: Notas a serem processadas (qualquer quantidade)
    :param sit: (opcional)situação da turma de acordo com a média da turma.
                a situação pode ser "boa", "regular", ou "ruim".
    :return: Retorna um dicionario com:
        - A maior nota
        - A menor nota
        - A média da turma
        - A situação da turma(opcional)
    """
    boletim = dict()
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['media'] = round(sum(n) / len(n), 1)
    if sit:
        if boletim['media'] >= 7:
            boletim['situação'] = 'boa'
        elif 7 > boletim['media'] >= 5:
            boletim['situação'] = 'regular'
        elif boletim['media'] < 5:
            boletim['situação'] = 'ruim'
    return boletim


print(notas(1.5, 5, 5, sit=True))