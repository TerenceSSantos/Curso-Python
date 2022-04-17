#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso você deve mostrar para cada palavra quais são as suas vogais.

lista = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar",
            "mercado", "programador", "futuro")
                                        #  *** SOLUÇÃO GUANABARA ***
for palavra in lista:                   # for p in palavras:
    vogais = ''                         #   print(f'\nNa palavra {p.upper()} temos ', end='')
    for i in range(0, len(palavra)):    #   for letra in p:
        if palavra[i] in 'AEIOUaeiou':  #       if letra.lower() in 'aeiiou':
            vogais += ' ' + palavra[i]  #           print(letra, end='')
    print('Na palavra {} temos {}'.format(palavra.upper().strip(), vogais))