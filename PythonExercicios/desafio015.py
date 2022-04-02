km = float(input('Quantos quilometros rodados? Km '))
dias = int(input('Quantos dias de aluguel? '))
total = (0.15 * km) + (dias * 60)
print('Total a pagar R$ {:.2f}'.format(total))