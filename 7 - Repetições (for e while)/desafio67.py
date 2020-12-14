# Mostrar a tabuada de vários números. O programa será parado quando o número for negativo

while True:
    tab = int(input('\033[34mQual tabuada quer ver?: \033[m'))
    if tab < 0:
        break
    for c in range(1, 11):
        print(f'{tab} x {c} = {tab * c}')
print('\nFim do programa')
