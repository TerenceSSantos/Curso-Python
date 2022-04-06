from datetime import date

ano_nasc = int(input('Por favor informe o seu ano de nascimento: '))
resultado = date.today().year - ano_nasc
if resultado == 18:
   print('Está no momento de você se alistar')
elif resultado > 18:
   print('Passou {} ano(s) do seu alistamento'.format(resultado - 18))
else:
   print('Falta(m) {} ano(s) para seu alistamento'.format(18 - resultado))