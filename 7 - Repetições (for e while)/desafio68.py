# Um jogo de PAR OU IMPAR. O programa só será interrompido quando o usuario perder
# No final, mostrar o total de vitórias consecultivas

from random import randint
ganhou = 0
print('-' * 30)
print('Vamos jogar \033[1:33mPar ou impar\033[m?')
print('-' * 30)
while True:
    val = int(input('Quantidade: '))
    while val < 0:
        val = int(input('Quantidade: '))
    PoI = str(input('Par ou impar?: '))[0]
    while PoI not in 'pPiI':
        PoI = str(input('Par ou impar?: '))[0]
    val_comp = randint(0, 10)
    total = val_comp + val
    print(f'\nEu joguei {val_comp} e você {val}, dando {total}.')
    if (total % 2 == 0 and PoI in 'Pp') or (total % 2 != 0 and PoI in 'Ii'):
        print('Você \033[32mGANHOU!\033[m')
        ganhou += 1
    else:
        print('Você \033[31mPERDEU!\033[m')
        break
    print('-' * 30)
if ganhou > 2:
    print(f'\n\033[32mVocê ganhou {ganhou} seguidas\033[m')
elif ganhou == 1:
    print(f'\nVocê ganhou uma vez')
else:
    print(f'\nVocê perdeu miseravelmente')
