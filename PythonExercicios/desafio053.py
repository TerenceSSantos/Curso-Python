# Exercício para verificar se uma frase é um palíndromo, desconsiderando os espaços
# Exemplos:
# apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona

print('='*60)
frase = str(input('Digite uma frase: \n')).strip()
frase = frase.replace(' ','') # Substituir os espaços por "NÃO-ESPAÇO"
#  alternativa a opção acima
# frase = frase.split()
# junto = ''.join(frase)
tamanho = len(frase)
frase2 = str() # estava dando erro de variável desconhecida então declarei fora do for
for i in range(tamanho-1, -1, -1): # Opção sem este for => inverso = junto[::-1]
   frase2 += frase[i]
if frase.upper() == frase2.upper():
   print('É um palíndromo')
else:
   print('Não é um palíndromo')
