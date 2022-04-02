alt = float(input('Digite a altura da parede: '))
compr = float(input('Digite o comprimento da parede: '))
area = alt * compr
qt_tinta = area / 2
print('Será preciso {} litros de tinta para pintar {} metros quadrados de parede'.format(qt_tinta, area))