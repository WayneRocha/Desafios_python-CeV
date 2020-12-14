# fazer uma tupla com 20 números(escritos por extenso) e mostra para o usuario informar um numero nesse intervalo
# e mostrar o numero que a pessoa digitou por extenso

while True:
    n_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                 'onze', 'doze', 'treze', 'quatorze ou catorze', 'quinze', 'dezesseis', 'dezessete',
                 'dezoito', 'dezenove', 'vinte')
    while True:
        num = int(input('Digite um número[1~20]: '))
        if 0 <= num <= 20:
            break
        print('\033[31mDeve ser entre 1 e 20\033[m')
    print(f'\n\033[4mO numero {num} se lê \033[1:33m{n_extenso[num]}\033[m\n')
    while True:
        continuar = str(input('Quer ver outro número? '))[0].upper()
        if continuar in 'NS':
            break
    print('\n')
    if continuar in 'N':
        break
