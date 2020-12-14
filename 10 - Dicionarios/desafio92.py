# ler... nome, ano de nascimento e carteira de trabalho(cadastrar a idade a partir do ano)
# Se o individuao tiver CTPS, ler ano de contratação e o salario.
# calcular a idade e acrescentar, tirando a idade, com quantos anos a pessoa vai se aposentar(35 anos de contribuição)

from datetime import date
dados = dict()
dados['Nome'] = str(input("Seu nome: ")).strip().title()
dados['ano_nascimento'] = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - dados['ano_nascimento']
print('-' * 30)
while True:
    tem_cartera = str(input('Tem cateira de trabalho?: ')).strip().upper()[0]
    if tem_cartera in 'SN':
        if tem_cartera in 'S':
            while True:
                dados['N_carteira'] = str(input('Número da CTPS: '))
                if dados['N_carteira'].isnumeric() and len(dados['N_carteira']) == 5:
                    break
                else:
                    if not dados['N_carteira'].isnumeric():
                        print('\033[31mPor favor, digite apenas números!\033[m\n')
                    elif len(dados['N_carteira']) < 5:
                        print(f'\033[31mEsta faltando {5 - len(dados["N_carteira"])} Números!\033[m\n')
                    elif len(dados['N_carteira']) > 5:
                        print(f'\033[31mVocê digitou {len(dados["N_carteira"]) - 5} Números a mais!\033[m\n')
            while True:
                dados['ano_contratacao'] = int(input('Ano de contratação: '))
                if date.today().year >= dados['ano_contratacao'] > dados['ano_nascimento']:
                    break
                else:
                    print('\033[31mAno invalido! Tente novamente\033[m\n')
            while True:
                dados['salario'] = float(input('Salário: \033[32mR$\033[m'))
                if dados['salario'] > 0:
                    break
                else:
                    print('\033[31mSalario invalido! Tente novamente\033[m\n')
            dados['idade_aposento'] = (dados['ano_contratacao'] - dados['ano_nascimento']) + 35
            dados['ano_aposento'] = dados['idade_aposento'] + dados['ano_nascimento']
            break
        else:
            break
print('=' * 40)
print(f'{"Nome":.<20}{dados["Nome"]}')
print(f'{"Idade":.<20}{dados["Idade"]} Anos')
if tem_cartera in 'S':
    print(f'{"PIS/PASEP":.<20}{dados["N_carteira"]}')
    print(f'{"Contratação em":.<20}{dados["ano_contratacao"]}')
    print(f'{"Salário":.<20}R${dados["salario"]:.2f}')
    print(f'{"Se aposenta em":.<20}{dados["ano_aposento"]}, com {dados["idade_aposento"]} anos')
