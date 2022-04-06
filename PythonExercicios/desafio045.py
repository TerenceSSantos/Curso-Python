from random import choice
from sre_parse import parse_template

print('Vamos jogar Jokenpô - Faça sua escolha')
computador = choice(['tesoura', 'papel', 'pedra'])
print('==='* 20)
print('1 = tesoura')
print('2 = papel')
print('3 = pedra')
print('==='* 20)
escolha = int(input())

if escolha > 3:
   print('Opção inválida')
else:
   if escolha == 1:
      eu = 'tesoura'
   elif escolha == 2:
      eu = 'papel'
   elif escolha == 3:
      eu = 'pedra'
      
   if (computador == 'tesoura' and eu == 'tesoura') or (computador == 'pedra' and eu == 'pedra') or (computador == 'papel' and eu == 'papel'):
      print('Escolhi {} e você {}. EMPATAMOS'.format(computador, eu))
   if (computador == 'tesoura' and eu == 'papel') or (computador == 'pedra' and eu == 'tesoura') or (computador == 'papel' and eu == 'pedra'):
      print('Escolhi {} e você {}. GANHEI!!'.format(computador, eu))
   if (computador == 'tesoura' and eu == 'pedra') or (computador =='pedra' and eu == 'papel') or (computador == 'papel' and eu == 'tesoura'):
      print('Escolhi {} e você {}. Parabéns, você GANHOU!'.format(computador, eu))

