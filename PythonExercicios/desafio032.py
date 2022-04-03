from calendar import isleap
# incremento
from datetime import date

ano = int(input('Por favor informe um ano: '))
#incremento
if ano == 0:
    ano = date.today().year # pegar data (ano) atual do computador
if isleap(ano):
    print(ano,'é um ano bissexto')
else:
    print(ano, 'não é um ano bissexto')