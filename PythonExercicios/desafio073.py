#   Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
#   na ordem de colocação. Depois mostre:
#   A) Apenas os 5 primeiros colocados.
#   B) Os últimos 4 colocados da tabela.
#   C) Uma lista com os times em ordem alfabética.
#   D) Em que posição na tabela está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG',
         'Botafogo', 'Atlético_PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí',
         'Ponte Preta', 'Atlético-GO')
print('=' * 60)
print(f'Times do Brasileirão 2017: {times}')
print('=' * 60)
print(f'Os 5 primeiros são: {times[:5]}')
print('=' * 60)
print(f'Os 4 últimos são: {times[-4:]}')
print('=' * 60)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 60)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('=' * 60)