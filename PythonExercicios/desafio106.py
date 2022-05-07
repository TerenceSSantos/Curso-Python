#   Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
#   manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa encerrará. OBS: use cores.

def infoHelp(comando):
    titulo = f'Acessando o manual do comando "{comando}"'
    print('\033[41m-' * (len(titulo) + 4))
    print('  ' + titulo)
    print('-' * (len(titulo) + 4))
    print('\033[45m')
    help(comando)



titulo = 'SISTEMA DE AJUDA PyHELP'
while True:
    print('\033[44m=' * (len(titulo) + 4))
    print('  ' + titulo)
    print('=' * (len(titulo) + 4))
    comando = input('\033[mFunção ou Biblioteca: ')
    if comando == 'FIM' or comando == 'fim':
        break
    infoHelp(comando)
