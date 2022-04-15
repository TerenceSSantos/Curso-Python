# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('='*60)
termo = int(input('Informe o 1º termo: '))
razao = int(input('Informe a razão: '))
i = 1
impressao = str(termo)
while i < 10:
    impressao = impressao + ' ' + str(termo + razao)
    termo = termo + razao
    i += 1
print(impressao)