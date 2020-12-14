# Ler o ano de nascimento e mostrar se o voto é negado | opcional | obrigatório |

from datetime import date


def voto(ano_nasc):
    '''
    ==> De acordo com o ano de nascimento, é verificado se o voto é obrigatório, opcional ou é negado
        :param ano_nasc: Ano de nascimento(ex:1980)
        :return: retorna a frase "Com ... anos seu voto é ..."
    '''
    idade = date.today().year - ano_nasc
    if idade >= 18:
        return f'Com {idade} anos seu voto é OBRIGATÓRIO'
    elif idade < 16:
        return f'Com {idade} anos seu voto é NEGADO'
    elif idade >= 65:
        return f'Com {idade} anos seu voto é OPCIONAL'
    else:
        return f'Com {idade} anos seu voto é OPCIONAL'


while True:
    ano_nascimento = int(input('Ano de nascimento: '))
    if ano_nascimento <= date.today().year:
        break
    else:
        print('\033[31mAno inválido\n\033[m')
print(voto(ano_nascimento))
