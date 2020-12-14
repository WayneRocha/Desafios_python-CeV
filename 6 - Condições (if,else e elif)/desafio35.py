# ler o comprimento de 3 retas e dizer se é possivel formar um triagulo
# Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas
print('é um triangulo?')
print('¨' * 15)
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
print('-' * 15)
if r1 + r2 > r3:
    print('Pode formar um \033[35mTriangulo!\033[m')
else:
    print('não pode formar um \033[35mtriangulo\033[m :( ')
