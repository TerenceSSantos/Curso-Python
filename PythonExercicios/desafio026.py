frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição', frase.find('A') + 1)
print('A letra "A" aparece pela última vez na posição', frase.rfind('A') + 1)
print('O tamanho da frase é:', len(frase))