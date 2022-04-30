#   Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
#   em um dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import  itemgetter

sorteio = {
    'jogador 1':randint(1, 6),
    'jogador 2':randint(1, 6),
    'jogador 3':randint(1, 6),
    'jogador 4':randint(1, 6)
}
ranking = list()
print(f'{"Valores sorteados":=^60}')
for k, v in sorteio.items():
    sleep(1.0)
    print(f'O {k} tirou {v}')

print(f'{"Ranking dos jogadores":-^60}')

ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True) # itemgetter(1) pelo valor - itemgetter(0) pela chave

for i, v in enumerate(ranking):
    sleep(1.0)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
print()
print(ranking)