#   Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
#   mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('='*60)
print('{:^60}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('='*60)
jogador = computador = soma = cont = 0
par_impar = ''
while True:
    computador = randint(0, 11)
    jogador = int(input('Diga um valor: '))
    par_impar = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print('-'*60)
    soma = jogador + computador
    if (soma % 2 == 0 and par_impar == 'P'):
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}. DEU PAR')
        print('-' * 60)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
        print('=-' * 30)
    elif (soma % 2 != 0 and par_impar == 'I'):
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}. DEU ÍMPAR')
        print('-' * 60)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
        print('=-' * 30)
    elif (soma % 2 == 0 and par_impar == 'I'):
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}. DEU PAR')
        print('Você PERDEU!')
        break
    elif (soma % 2 != 0 and par_impar == 'P'):
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}. DEU ÍMPAR')
        print('Você PERDEU!')
        break
print('=-' * 30)
print(f'GAME OVER! Você venceu {cont} vezes')