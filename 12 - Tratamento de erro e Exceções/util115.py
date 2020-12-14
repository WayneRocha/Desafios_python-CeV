
maiornome = 0


def menu():
    print('-' * 30)
    print(f'{"Menu principal":^30}')
    print('-' * 30)
    print('\033[34m[1]\033[m - Ver pessoas cadastradas')
    print('\033[34m[2]\033[m - Cadastrar uma pessoa')
    print('\033[34m[3]\033[m - Sair ')
    while True:
        try:
            opcao = int(input('\033[34mOpção: \033[m'))
        except:
            pass
        else:
            if 1 <= opcao <= 3:
                break
    return opcao


def cadastrar(pessoa, pessoas):
    global maiornome

    while True:
        try:
            pessoa['nome'] = str(input('Nome: ')).strip().title()
        except KeyboardInterrupt:
            print('\033[31mDigite o nome da pessoa\033[m')
        except:
            print('\n\033[31mOcorreu um erro, tente novamente\033[m\n')
            menu()
        else:
            if pessoa['nome'] == '':
                print('\033[31mDigite o nome da pessoa\033[m')
            else:
                break
    while True:
        try:
            pessoa['idade'] = int(input('Idade: '))
        except KeyboardInterrupt:
            print('\033[31mDigite a idade da pessoa\033[m')
        except ValueError:
            print('\033[31mIdade invalida, tente novamente\033[m')
        except:
            print('\n\033[31mOcorreu um erro, tente novamente\033[m\n')
            menu()
        else:
            if pessoa['idade'] >= 0:
                break
            else:
                print('\033[31mIdade invalida, Não existem anos negativos\033[m')
    pessoas.append(pessoa.copy())
    salvar(pessoa)
    if len(pessoa['nome']) > maiornome:
        maiornome = len(pessoa['nome'])


def listarPessoas(pessoas):
    if len(pessoas) > 0:
        print(f'{"Nome":^20}{"Idade":^}')
        for person in pessoas:
            nome_pessoa = person['nome']
            idade_pessoa = person['idade']
            print(f'{nome_pessoa:.<20}{idade_pessoa:^5}')
    else:
        print('Nenhuma pessoa cadastrada')


def salvar(pessoa):
    banco_de_dados = open('cadastrosd115.txt', 'a')
    banco_de_dados.write(f'{pessoa["nome"]} ')
    banco_de_dados.write(f'{pessoa["idade"]}')
    banco_de_dados.write(';')


def restaurarPessoas():
    pessoas = list()
    pessoa = dict()
    a = open('cadastrosd115.txt', 'r').readline()
    if a == '':
        return []
    lista_pessoas = a.split(';')
    del lista_pessoas[-1]
    for p in lista_pessoas:
        dados_pessoa = p.split(' ')
        pessoa['nome'] = dados_pessoa[0]
        pessoa['idade'] = dados_pessoa[1]
        pessoas.append(pessoa.copy())
    return pessoas


def sair():
    exit()


