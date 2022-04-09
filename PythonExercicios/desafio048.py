#  Calcular a soma de todos os números ímpares que são múltiplos de 3 e que estão no intervalo de 1 à 500

print('='*60)
soma = 0
for i in range(1, 501, 2):
   if (i % 3) == 0:
      soma += i
      print(i) # mostrar quem são
print('Total do múltiplos de 3: ',soma)