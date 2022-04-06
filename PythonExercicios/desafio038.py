n1 = int(input('Por favor informe um número inteiro: '))
n2 = int(input('Por favor informe outro número inteiro: '))
if n1 > n2:
   print('O 1º número {} é maior que o 2º {}'.format(n1, n2))
elif n2 > n1:
      print('O 2º {} número é maior que o 1º {}'.format(n2, n1))
else:
   print('Os 2 números são iguais')