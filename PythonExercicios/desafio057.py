#   Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#   Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo [F/M]: ')).upper().strip()[0] # posição zero
# while ((sexo != 'F') and (sexo != 'M')):
while sexo not in 'FM':
    sexo = str(input('Inválido. \nDigite seu sexo novamente [F/M]: ')).upper().strip()[0]
print('-'*50)
print('Fim de programa. Você digitou', sexo)