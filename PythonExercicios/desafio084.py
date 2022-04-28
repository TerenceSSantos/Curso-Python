#   Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
#   A) Quantas pessoas foram cadastradas.
#   B) Uma listagem com as pessoas mais pesadas.
#   C) Uma listagem com as pessoas mais leves

print('=' * 60)
individuo = list()
pessoas = list()
maior = menor = i = 0
while True:
    nome = str(input('Nome: ')).strip()
    peso = float(input('Peso: '))
    if i == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    individuo.append(nome)
    individuo.append(peso)
    pessoas.append(individuo[:])
    individuo.clear()
    i += 1
    continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Nn':
        break
mais = []
menos = []
print('-' * 60)
for p in pessoas:
    print('Aqui está o indivíduo', p)
    if maior == p[1]:
        mais.append(p[0])
    if menor == p[1]:
        menos.append(p[0])
print('-' * 60)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print('O maior peso foi de {:.1f}KG. Peso de {}'.format(maior, mais))
print('O menor peso foi de {:.1f}KG Peso de {}'.format(menor, menos))
print('-' * 60)
print(f'A seguir a lista de pessoas completa:\n{pessoas}')