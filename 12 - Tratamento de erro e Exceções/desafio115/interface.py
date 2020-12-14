def menu():
    print('-' * 30)
    print('Menu principal'.center(30))
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


def listarPessoas(pessoas):
    if len(pessoas) > 0:
        print(f'{"Nome".center(20)}{"Idade":^}')
        for person in pessoas:
            nome_pessoa = person['nome']
            idade_pessoa = person['idade']
            print(f'{nome_pessoa:.<20}{idade_pessoa.center(5)}')
    else:
        print('Nenhuma pessoa cadastrada')


def sair():
    print('Muito obrigado, volte sempre! :)')
    exit()
