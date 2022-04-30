#   Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
#   Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#   Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

print('=' * 60)
trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: ')).strip()
ano = int(input('Ano de nascimento: '))
trabalhador['Idade'] = date.today().year - ano
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['Aposentadoria'] = int((trabalhador['Contratação'] + 35) - ano)

print('-' * 120)
print(trabalhador)
print('-' * 120)

for k, v in trabalhador.items():
    print(f' * {k} tem o valor {v}')
