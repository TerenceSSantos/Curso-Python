#   Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
#   vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final mostre o conteúdo
#   das 3 listas geradas

print('=' * 60)
lista_completa = []
lista_par = []
lista_impar = []
while True:
    lista_completa.append(int(input('Digite um número: ')))
    continua = str(input('Quer continuar? [S/N]: '))
    if continua in 'Nn':
        break
for lista in lista_completa:
    if lista % 2 == 0:
        lista_par.append(lista)
    else:
        lista_impar.append(lista)
print('=' * 60)
print(f'A lista completa é {lista_completa}')
print('-' * 60)
print(f'A lista de pares é: {lista_par}')
print('-' * 60)
print(f'A lista de ímpares é: {lista_impar}')