from interface import menu


def restaurarPessoas():
    pessoas = list()
    pessoa = dict()
    a = open('cadastros.txt', 'r').readline()
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


def cadastrar(pessoa, pessoas):
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


def salvar(pessoa):
    banco_de_dados = open('cadastros.txt', 'a')
    banco_de_dados.write(f'{pessoa["nome"]} ')
    banco_de_dados.write(f'{pessoa["idade"]}')
    banco_de_dados.write(';')
    banco_de_dados.close()
