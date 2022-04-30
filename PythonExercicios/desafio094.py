#   Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
#   e todos os dicionários em uma lista. No final mostre:
#   A) Quantas pessoas foram cadastradas.
#   B) A média de idade do grupo.
#   C) Uma lista com todas as mulheres.
#   D) Uma lista com todas as pessoas com idade acima da média.

print('=' * 60)
pessoa = {} # dicionario
gente = [] # lista
mulheres = list()
continuar = 'S'
soma = media = 0
while True:
    pessoa['Nome'] = str(input('Nome: ')).strip()
    pessoa['Sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    while pessoa['Sexo'] not in 'FfMm':
        pessoa['Sexo'] = str(input('Digite apenas "F" ou "M"'))
    pessoa['Idade'] = int(input('Idade: '))
    if pessoa['Sexo'] in 'Ff':
        mulheres.append(pessoa['Nome'])
    media += pessoa['Idade']
    gente.append(pessoa.copy())
    soma += 1
    continuar = str(input('Deseja continuar? [S/N]: '))
    while continuar not in 'NnSs':
        continuar = str(input('Deve digitar apenas "S" ou "N": '))
    if continuar in 'Nn':
        break

print('-' * 60)
print(gente)
print(f' - O grupo tem {soma} pessoas.')
print(f' - A média de idade é de {media/soma:.2f} anos')
print(f' - As mulheres cadastradas foram: {mulheres}')
print(' - Lista das pessoas que estão acima da média: ')
for i, v in enumerate(gente):
    for dicio in v.items():
        if v['Idade'] > media / soma:
            print(f'{dicio[0]} = {dicio[1]};', end=' ')
    print()
print(f'{"FIM DE PROGRAMA":-^60}')