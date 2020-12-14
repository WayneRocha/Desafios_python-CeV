# ler um nome de uma cidade e dizer se começa ou não com a palavra 'santo'

cidade = str(input('Nome da sua cidade: ')).strip()
print('¨¨' * 10)
print(f"Começa com \033[4m'Santo'\033[m: {cidade[:5].upper() == 'SANTO'}", )
