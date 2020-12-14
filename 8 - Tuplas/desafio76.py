# Tupla com nomes dos produtos e mostra-lo de forma tabular

produtos = ('Lápis', 1.00, 'Borracha', 0.50, 'Caneta', 1.50, 'Lapisera', 2.00, 'Apontador', 3.00, 'Estojo', 5.00,
            'Caderno(1 materia)', 10.00, 'caderno(10 materias)', 20.00, 'mochila', 50.00)
print('=' * 31)
print(f'{"Tabela de preços":^31}')
print('=' * 31)
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<25} R${produtos[c + 1]:.2f}')
