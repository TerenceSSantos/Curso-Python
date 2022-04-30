#   Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
#   No final mostre o conteúdo da estrutura na tela
#   REPLICAR:
'''
Nome: Joaquim
Média de Joaquim: 4.5
Nome é igual a Joaquim
Média é igual a 4.5
Situação é igual a Reprovado
'''

print('=' * 60)
aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print('-' * 60)
print(f'O nome é {aluno["Nome"]}')
print(f'A média é de {aluno["Média"]}')
if aluno['Média'] >= 6:
    print('Situação: APROVADO(A)')
    aluno['Situação'] = 'APROVADO(A)'
elif aluno['Média'] >= 5:
    print('Situação: RECUPERAÇÃO')
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    print('Situação: REPROVADO(A)')
    aluno['Situação'] = 'REPROVADO(A)'
print('-' * 60)
print(aluno)