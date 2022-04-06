n1 = float(input('Inoforme a 1ª nota:'))
n2 = float(input('Informe a 2ª nota: '))
media = (n1 + n2) / 2
if media >= 7:
   print('Média {:.1f}, aluno APROVADO'.format(media))
elif media >= 5 and media < 7:
   print('Média {:.1f}, aluno em recuperação'.format(media))
else:
   print('Média {:.1f}, aluno REPROVADO'.format(media))