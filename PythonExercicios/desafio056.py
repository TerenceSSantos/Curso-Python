#  Ler nome, idade, sexo de 5 pessoas
#  mostrar a média de idade
#  nome do homem mais velho
#  quantas mulheres tem menos de 20 anos

print('='*60)
nome = []
idade = []
sexo = [] 
for i in range(0, 5):
   nome += [str(input('Por favor informe um nome: '))]
   idade += [str(input('Por favor informe a idade: '))]
   print('Informe o sexo')
   print('F - para feminino')
   print('M - para masculino\n')
   sexo += [str(input('Informe o sexo: ')).upper()]
   print('-'*60)

media = int(0)
for i in range(0, 5):
   media = media + int(idade[i])

maior_idade = int(0)
indice = int(0)
cont = int(0)
for i in range(0, 5):
   if sexo[i] == 'M':
      if maior_idade < int(idade[i]):
         maior_idade = int(idade[i])
         indice = i
   if sexo[i] == 'F':
      if int(idade[i]) < 20:
         cont += 1

mais_velho = max(idade)

print('A média de idade é de {:.2f}'.format(media/5))
print('O homem mais velho é o {} com {} anos'.format(nome[indice], maior_idade))
print('Temos {} mulher(es) com menos de 20 anos'.format(cont))
print('{:-^60}'.format('Impressão das listas'))
print(nome)
print(idade)
print(sexo)