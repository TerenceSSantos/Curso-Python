#   Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

from prime_test import prime

print('{:=^60}'.format(' COM BIBLIOTECA '))
n = int(input('Digite um número inteiro: '))
if prime.test(n):
   print('{} é um número primo'.format(n))
else:
   print('{} não é um número primo'.format(n))


print('{:=^60}'.format(' PENSADO POR MIM '))
if n == 2:
   print(n, 'é um número primo')
elif n == 1:
   print(n, 'não é um número primo')
else:
   cont = 0
   for i in range(1, n + 1):
      if n % i == 0:
         cont += 1
   if cont > 2:
      print('{} NÃO é um nº primo'.format(n))
   else:
      print('{} é um nº primo'.format(n))