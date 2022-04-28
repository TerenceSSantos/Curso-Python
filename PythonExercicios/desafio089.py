#   Crie um programa que leia nome e 2 notas de vários alunos e guarde tudo em uma lista composta.
#   No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
#   notas de cada aluno individualmente.

print('=' * 60)
aluno = [[], [], []]
notas = []
media = 0
continua = ''
contador = 0
while True:
    soma = 0
    aluno[0].append(str(input('Nome: ')).strip())
    for i in range(0, 2):
        notas.append(float(input(f'Nota {i+1}: ')))
        soma += notas[i]
    media = soma / 2
    aluno[1].append(notas[:])
    notas.clear()
    aluno[2].append(media)
    contador += 1
    continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Nn':
        break

print('=' * 60)

print('{:<3} {:<10} {:>6}'.format('Nº', 'NOME', 'MÉDIA'))
for i in range(0, contador):
    print('{:<3} {:<10} {:>6}'.format(i + 1, aluno[0][i], aluno[2][i]))
print('-' * 60)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    print(f'Notas de {aluno[0][mostrar-1]} são {aluno[1][mostrar-1]}')
    print('-' * 60)
print('{:=^60}'.format(' PROGRAMA FINALIZADO '))