#CTRL+C CTRL+V do desafio 035

r1 = float(input('informe um valor: '))
r2 = float(input('informe outro valor: '))
r3 = float(input('informe outro valor: '))

if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):
    print('Nao é um triangulo')
elif (r1 == r2) and (r1 == r3) :
    print('É um triângulo Equilatero')
elif (r1==r2) or (r1==r3) or (r2==r3):
    print('É um triângulo Isósceles')
else:
    print('É um triângulo Escaleno')