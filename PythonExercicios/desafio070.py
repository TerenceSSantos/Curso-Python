#   Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
#   o usuário vai continuar. No final mostre:
#   A)  Qual é o total gasto na compra.
#   B)  Quantos produtos custam mais de R$ 1.000,00.
#   C)  Qual é o nome do produto mais barato.

print('=' * 40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('=' * 40)
continuar = 'S'
produto = nome_barato = ''
preco = total = qt_caro = barato = contador = 0
while continuar == 'S':
    contador += 1
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        qt_caro += 1
    if contador == 1 or preco < barato:
        barato = preco
        nome_barato = produto
    '''elif preco < barato:
        barato = preco
        nome_barato = produto   '''

    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar not in 'SN':
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]

print('{:=^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {qt_caro} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {nome_barato} que custa R$ {barato:.2f}')