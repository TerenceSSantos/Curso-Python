#   Faça um programa que tenha uma função chamada ficha(), que receba 2 parâmetros opcionais: o nome de um jogador
#   e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
#   não tenha sido informado corretamente.

def ficha(jogador='', gol=0):
    if jogador == '':
        jogador = '< desconhecido>'
    print('-' * 60)
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato')
    print('-' * 60)


#   PROGRAMA PRINCIPAL
print('=' * 60)
jog = str(input('Nome do Jogador: ')).strip()
qt_gol = str(input('Número de Gols: '))
if qt_gol.isnumeric():
    qt_gol = int(qt_gol)
else:
    qt_gol = 0
ficha(jog, qt_gol)
