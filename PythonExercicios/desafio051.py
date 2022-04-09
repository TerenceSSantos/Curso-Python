#  Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#  No final, mostre os 10 primeiros termos dessa progressão.

print('='*60)
termo = int(input('Informe o 1º termo para cálculo da progressão aritmética: '))
razao = int(input('Informe a razão: '))
print('='*60)
for i in range(0, razao * 10, razao):
   print(termo)
   termo += razao
