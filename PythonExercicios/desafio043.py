alt = float(input('Informe a sua altura '))
peso = float(input('Informe o seu peso '))
imc = peso / (pow(alt, 2))
if imc < 18.5:
   print('{:.2f}. Abaixo do peso'.format(imc))
elif imc >= 18.5 and imc< 25:
   print('{:.2f}. Peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
   print('{:.2f}. Sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
   print('{:.2f}. Obesidade'.format(imc))
else:
   print('{:.2f}. Obesidade Mórbida')