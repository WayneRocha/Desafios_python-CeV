# ler o nome, a idade e sexo de 4 pessoas. e mostrar
# a média de idade do grupo | Qual o nome do homem mais velho | Quantas mulheres tem menos de 21 anos

MediaIdade = 0
MaiorIdade = 0
HomVelho = ''
MulhMenos20 = 0
for c in range(1, 5):
    print(f'------ {c}ªpessoa ------')
    nome = str(input('Qual o seu nome?: ')).strip().capitalize()
    idade = int(input('Qual a sua idade?: '))
    MediaIdade += idade
    sexo = str(input('Qual é o seu sexo?[f/m]: ')).strip().upper()
    if sexo != 'F' or 'M':
        print('Opção invalida\nTente novamente')
        exit()
    if idade > MaiorIdade:
        MaiorIdade = idade
        HomVelho = nome
    if sexo == 'F' and idade <= 21:
        MulhMenos20 += 1
MediaIdade /= 4
print(f'A idade média das 4 pessoas é {MediaIdade} Anos')
print(f'O {HomVelho} é o homem mais velho')
if MulhMenos20 == 0:
    print('Nenhuma mulher tem menos de 20 anos')
print(f'{MulhMenos20} mulheres tem menos de 20 anos')
