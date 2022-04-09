#  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
#  Se o valor digitado for ímpar, desconsidere-o.

print('='*60)
soma = 0
for i in range(1, 7):
   n = int(input('Digite um nº inteiro: '))
   if (n % 2) == 0:
      soma += n
print('A soma dos números deu: {}'.format(soma))