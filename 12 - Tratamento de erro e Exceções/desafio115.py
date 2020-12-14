import util115 as u
pessoa = dict()


pessoas = u.restaurarPessoas()
while True:
    opcao = u.menu()
    if opcao == 1:
        u.listarPessoas(pessoas)
    elif opcao == 2:
        u.cadastrar(pessoa, pessoas)
    else:
        u.sair()
