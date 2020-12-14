# ler um valor, e passar por uma função para validar um número inteiro

def leiaInt(pergunta):
    """
    -> lê apenas um número inteiro
    :param pergunta: Frase que será mostrada, para o usuario dar a entrada do dado
    :return: Se o usuario digitar um numero inteiro, ele retorna esse numero,
             caso contrário, o programa pedirá para ler novamente até que seja digitado um numero inteiro.
    """
    while True:
        num = input(pergunta)
        if num.isnumeric():
            return int(num)
        else:
            print('\033[31mValor invalido!\033[m\n')


n = leiaInt('Digite um valor: ')
print(f'Você digitou o valor {n}')
