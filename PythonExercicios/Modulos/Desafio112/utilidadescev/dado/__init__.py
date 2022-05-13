def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        msg = str(msg).replace(',', '.')
        teste = str(msg).replace('.', '')
        if teste.isnumeric():
            valor = float(msg)
            ok = True
        elif msg.isspace() or msg == '':
            msg = str(input('\033[31m ERRO! "vazio" é um preço inválido: \033[m '))
        else:
            msg = str(input(f'\033[31m ERRO! {msg} é um preço inválido: \033[m '))
        if ok:
            break
    return valor
