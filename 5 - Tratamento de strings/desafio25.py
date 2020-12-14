# ler um nome e dizer se tem 'silva' no nome

nome = str(input('Qual seu nome? ')).strip()
print(f'Tem \033[1m"silva"\033[m: {"silva" in nome.lower()}')
