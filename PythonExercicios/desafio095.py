#   Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
#   detalhes do aproveitamento de cada jogador.

print(f'{" APRIMORANDO O DESAFIO 093 ":=^60}')
gol = list()
jogador = dict()
estatistica = list()
while True:
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().upper()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    print('-' * 60)
    soma = 0
    for i in range(1, partidas + 1):
        gol.append(int(input(f'Quantos gols na partida {i}ª')))
        soma += gol[i - 1]
    jogador['Gols'] = gol[:]
    jogador['Total'] = soma
    estatistica.append(jogador.copy())
    gol.clear()
    continuar = str(input('Deseja continuar? [S/N] '))
    while continuar not in 'SsNn':
        continuar = str(input('Deve digitar apenas "S" ou "N": '))
    print('-' * 60)
    if continuar in 'Nn':
        break

print('=' * 60)
print(f'{"Cod":<3} {"Nome":<20} {"Gols":<18} {"Total":>3}')
print('-' * 60)
for i, est in enumerate(estatistica):
    print(f'{i:<3} {est["Nome"]:<20} {str(est["Gols"]):<18} {est["Total"]:>3}')

while True:
    print('-' * 60)
    escolha = int(input('Mostrar dados de qual jogador? (999 para encerrar! )'))
    if escolha == 999:
        break
    if escolha < 0 or escolha > (len(estatistica) - 1):
        print(f'ERRO! Não existe jogador com o código {escolha}! Tente Novamente.')
    else:
        for i, est in enumerate(estatistica):
            if escolha == 999:
                break
            if escolha == i:
                print(f'LEVANTAMENTO DO JOGADOR {est["Nome"]}')
                for j in range(0, len(est["Gols"])):
                    print(f'No jogo {j} fez {est["Gols"][j]} gol(s).')

print(f'{" PROGRAMA ENCERRADO ":*^60}')

print('*' * 60)
print()
for jog in estatistica:
    print(jog)
print('*' * 60)
