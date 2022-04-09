print('==='*40)
num = int(input('Informe um número inteiro: '))
print('==='*20)
print('Digite 1 para converter para binário')
print('Digite 2 para converte para octal')
print('Digite 3 para converter para hexadecimal')
print('Digite 4 para converter todos')
print('==='*20)
opcao = int(input('Sua opção: '))
print('==='*20)
binario = bin(num)
octal = oct(num)
hexa = hex(num)
if opcao == 1:
   print('{} em bínário é {}'.format(num, binario[2:]))
elif opcao ==2:
   print('{} em octal é {}'.format(num, octal[2:]))
elif opcao == 3:
   print('{} em hexadecimal é {}'.format(num, hexa[2:]))
elif opcao == 4:
   print('{} em bínário é {}'.format(num, binario[2:]))
   print('{} em octal é {}'.format(num, octal[2:]))
   print('{} em hexadecimal é {}'.format(num, hexa[2:]))
else:
   print('\033[1;31;40m Opção inválida!!\033[m')