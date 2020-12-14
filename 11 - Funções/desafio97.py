# Imprimir uma frase em forma de titulo com uma função

def faztitulo(texto, linha='-'):
    tam_linha = int((len(texto) + ((50 / 100) * len(texto))) / len(linha))
    print(linha * tam_linha)
    print(f'{texto:^{tam_linha * len(linha)}}')
    print(linha * tam_linha)


faztitulo('python!')
