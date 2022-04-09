# Ler o ano de nascimento de 7 pessoas
# Mostrar quantos são maiores de idade e quantos são menores

from datetime import date

print('='*60)
maior = int(0)
menor = int(0)
for i in range(0, 7):
   ano = int(input('Por favor digite o ano de nascimento: '))
   if ((date.today().year - ano) >= 18):
      maior += 1
   else:
      menor += 1
print('Temos {} maior(es) de idade'.format(maior))
print('Temos {} menor(es) de idade'.format(menor))