alt = float(input('Informe a sua altura '))
peso = float(input('Informe o seu peso '))
imc = peso / (pow(alt, 2))
if imc < 18.5:
   print('IMC de {:.2f}. Abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:   # 18.5 <= imc < 25 ====>MODO ALTERNATIVO DE ESCREVER<====
   print('IMC de {:.2f}. Peso ideal'.format(imc))
elif imc >= 25 and imc < 30:  # 25 <= imc < 30
   print('IMC de {:.2f}. Sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
   print('IMC de {:.2f}. Obesidade'.format(imc))
else:
   print('IMC de {:.2f}. Obesidade Mórbida')