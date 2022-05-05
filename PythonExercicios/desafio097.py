#   Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer com parâmetro e mostre
#   uma mensagem com tamanho adaptável.
#   Exemplo:
#   escreva('Olá Mundo!')
'''
    Saída:
    --------------------------
            Olá Mundo!
    --------------------------
'''


def escreva(frase, tamanho):
    tamanho += 4
    print('~' * tamanho)
    print(f'  {frase}')
    print('~' * tamanho)


frase = 'Terence S. dos Santos'
tamanho = len(frase)
escreva(frase, tamanho)

frase = 'Curso de Python no Youtube'
tamanho = len(frase)
escreva(frase, tamanho)

frase = 'CeV'
tamanho = len(frase)
escreva(frase, tamanho)

