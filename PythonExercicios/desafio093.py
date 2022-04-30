#   Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
#   e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
#   será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

print('=' * 60)
gol = list()
jogador = dict()
jogador['Nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
print('-' * 60)
soma = 0
for i in range(1, partidas + 1):
    gol.append(int(input(f'Quantos gols na partida {i}ª')))
    soma += gol[i - 1]  # sum(gol)
jogador['Gols'] = gol[:]
jogador['Total'] = soma
print('-' * 60)
print(jogador)
print('-' * 60)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 60)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas:')
for i in range(1, partidas + 1):
    print(f'  => Na {i}ª partida, fez {gol[i-1]} gols')
print(f'Foi um total de {jogador["Total"]} gols')
print('-' * 60)
