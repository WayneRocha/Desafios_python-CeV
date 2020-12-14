# Ler uma expressão númerica e dizer se ela é valida ou não

parenteses = []
colchetes = []
chaves = []
exp = str(input('Digite uma \033[34mexpressão númerica:\033[m '))
print(f'\n{exp}', end=' - ')
# 1ª verificação - quantidade iguais
if (exp.count('(') == exp.count(')')) and (exp.count('[') == exp.count(']')) and (exp.count('{') == exp.count('}')):
    for carac in exp:  # 2ª verificação - fechamento na ordem certa
        if carac == '(':
            parenteses.append('(')
        elif carac == '[':
            colchetes.append('[')
        elif carac == '{':
            chaves.append('{')
        if carac == ')':
            if len(parenteses) > 0:
                parenteses.pop()
        elif carac == ']':
            if len(colchetes) > 0:
                colchetes.pop()
        elif carac == '}':
            if len(chaves) > 0:
                chaves.pop()
    if len(parenteses) == 0 and len(colchetes) == 0 and len(chaves) == 0:
        print('\033[32mExpressão válida\033[m')
    else:
        print('\033[31mExpressão inválida\033[m')
else:
    print('\033[31mExpressão inválida\033[m')
