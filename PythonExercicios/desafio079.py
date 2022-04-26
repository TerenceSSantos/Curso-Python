#   Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
#   já exista ele não será adicionado. No final serão exibidos todos os valores únicos digitados em ordem crescente.

print('=' * 60)
lista = []  # list()
valor = i = 0
resposta = ''
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado. Não vou adicionar...')
    else:
        lista.insert(i, valor)
        i += 1
        print('Valor adicionado com sucesso')
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
lista.sort()
print('-' * 60)
print(f'Você digitou os valores {lista}')
print('-' * 60)
print(f'último da lista {lista[-1]}')