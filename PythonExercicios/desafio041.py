from datetime import date

ano_nasc = int(input('Informe o ano de nascimento do atleta:'))
idade = date.today().year - ano_nasc
if idade <= 9:
   print('Atleta de {} ano(s), categoria MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
   print('Atleta de {} ano(s), categoria INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
   print('Atleta de {} ano(s), categoria JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
   print('Atleta de {} ano(s), categoria SENIOR'.format(idade))
else:
   print('Atleta de {} ano(s), categoria MASTER'.format(idade))