# ler o ano de nascimento de um joven e informar de acordo com dia idade...
# se ele ainda vai se alistar no serviço militar
# se já é hora de se alistar
# se já passou oo tempo do alistamento
# e no final mostrar o tempo que falta ou passou do prazo

sexo = str(input('Qual seu sexo[f/m]? '))
if sexo == 'f' or 'F':
    print('Voçê não precisa se alistar')
    exit()
idade = int(input('Quantos anos vc tem? '))
idade_alistamento = 18
if idade == idade_alistamento:
    print('Você deve fazer o alistamento militar \033[31mIMEDIATAMENTE!\033[m')
elif idade > idade_alistamento:
    print(f'O alistamento militar está {idade - idade_alistamento} anos atrasado. \033[31mFAÇA IMEDIATAMENTE!\033[m')
elif idade < idade_alistamento:
    print(f'Faltam {idade_alistamento - idade} anos para seu alistamento militar')
