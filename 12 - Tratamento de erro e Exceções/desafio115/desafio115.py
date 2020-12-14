import interface
import sistema_de_dados
pessoa = dict()


pessoas = sistema_de_dados.restaurarPessoas()
while True:
    opcao = interface.menu()
    if opcao == 1:
        interface.listarPessoas(pessoas)
    elif opcao == 2:
        sistema_de_dados.cadastrar(pessoa, pessoas)
    else:
        interface.sair()
