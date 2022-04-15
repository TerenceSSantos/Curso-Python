# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

# PROGRAMA UM POUCO DIFERENTE DO SOLICITADO
resposta = 1
while resposta != 0:
    print('=' * 60)
    termo = int(input('Informe o 1º termo: '))
    razao = int(input('Informe a razão: '))
    i = 1
    impressao = str(termo)
    while i < 10:
        impressao = impressao + ' ' + str(termo + razao)
        termo = termo + razao
        i += 1
    print(impressao)
    print('Gostaria de fazer novamente?')
    print('[ 0 ] para encerrar')
    print('-' * 60)
    resposta = int(input('Qualquer outro Nº para continuar: '))

# EXERCÍCIO COMO SOLICITADO.
print('=' * 60)
termo = int(input('Informe o 1º termo: '))
razao = int(input('Informe a razão: '))
i = 1
impressao = str(termo)
repeticao = 10
mais_termo = repeticao
while mais_termo != 0:
    while i < int(repeticao):
        impressao = impressao + ' ' + str(termo + razao)
        termo = termo + razao
        i += 1
    print(impressao)
    mais_termo = int(input('Gostaria de ver mais quantos termos (ZERO PARA ENCERRAR)? '))
    repeticao = mais_termo
    i = 0
