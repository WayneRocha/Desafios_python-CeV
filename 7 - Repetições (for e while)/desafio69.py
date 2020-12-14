# cadastrar a idade e o sexo de varias pessoas. no final do cadastro perguntar se o úsuario quer continuar
# No final da execução. Retornar...
# Quantas pessoas tem + de 18 | Quantos homens foram cadastrados | Quantas mulheres tem menos de 20 anos

print('-' * 20)
print(f'{"CADASTRO":^20}')
print('-' * 20)
qt_maiores = qt_homens = qt_mulheres_20 = 0
while True:
    # cadastro do úsuario
    idade = int(input('Sua idade: '))
    while idade < 1:
        idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo[f/m]: '))[0]
    while sexo not in 'FfMm':
        sexo = str(input('Seu sexo[f/m]: '))[0]
    # estatisticas
    if idade > 18:
        qt_maiores += 1
    if sexo in 'Mm':
        qt_homens += 1
    elif (sexo in 'Ff') and (idade < 20):
        qt_mulheres_20 += 1
    #continuar ou não
    continuar = str(input('Quer continuar?: '))[0]
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar?: '))[0]
    if continuar in 'Nn':
        break
    print('=' * 25)
# Resultados
print('\033[34m-=' * 20)
print(f'{qt_maiores} Pessoas são maiores de 18 anos')
print('-=' * 20)
print(f'{qt_homens} Homens foram cadastrados')
print('-=' * 20)
print(f'{qt_mulheres_20} Pessoas tem menos de 20 anos\033[m')
