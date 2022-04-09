# Ler o peso de 5 pessoas
# mostrar o maior e menor peso

print('='*60)
pesado = float(0)
leve = float(10000)
for i in range(0, 5):
   peso = float(input('Por favor digite o peso em KG: '))
   if peso > pesado:
      pesado = peso
   if leve > peso:
      leve = peso
print('-'*60)
print('O maior peso é {}'.format(pesado))
print('O menor peso é {}'.format(leve))