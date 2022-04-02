import math

cat1 = float(input('Digite o valor do cateto Oposto: '))
cat2 = float(input('Digite o valor do cateto adjacente: '))
resultado = math.sqrt(pow(cat1, 2) + pow(cat2, 2))
print('O valor da hipotenusa é {} ou apenas {:.2f}'.format(resultado, resultado))
print('Usando math.hypot {} ou apenas {:.2f}'.format(math.hypot(cat1, cat2), math.hypot(cat1, cat2)))