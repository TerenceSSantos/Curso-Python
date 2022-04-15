#   Sequência de Fibonacci v1.0

#       VERSÃO FOR
print('='*60)
termo = int(input('Quantos termos da sequência de Fibonacci você quer? '))
anterior = 0
proximo = 1
impressao = ''
valor = 0

for i in range(0, termo):
    if i == 0:
        impressao = str(valor)
    elif i == 1:
        impressao = str(anterior) + '-' + str(proximo)
    elif i == 2:
        anterior = proximo
        impressao = impressao + '-' + str(proximo)
        proximo = anterior + proximo
    else:
        impressao = impressao + '-' + str(proximo)
        proximo += anterior
        anterior = proximo - anterior   

print('Versão com FOR:', impressao)

#   VERSÃO WHILE
print('{:=^60}'.format('VERSÃO WHILE'))
anterior = 0
proximo = 1
impressao = ''
valor = 0
i = 0
while i < termo:
    if i == 0:
        impressao = str(valor)
        i += 1
    elif i == 1:
        impressao = str(anterior) + '-' + str(proximo)
        i += 1
    elif i == 2:
        anterior = proximo
        impressao = impressao + '-' + str(proximo)
        proximo = anterior + proximo
        i += 1
    else:
        impressao = impressao + '-' + str(proximo)
        proximo += anterior
        anterior = proximo - anterior
        i += 1
print('Versão com WHILE: ',impressao)