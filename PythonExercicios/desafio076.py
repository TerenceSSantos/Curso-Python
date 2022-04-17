#   Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
#   No final mostre uma listagem de preços,organizando os dados em forma tabular.

produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('-' * 60)
print('{:^60}'.format('LISTAGEM DE PREÇOS'))
print('-' * 60)
for i in range(0, len(produtos), 2):
    print('{:.<45} R$ {:>10.2f} '.format(produtos[i], produtos[i+1]))
print('-' * 60)