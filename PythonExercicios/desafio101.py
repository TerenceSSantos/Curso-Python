#   Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
#   de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
#   nas eleições.

def voto(nasc):
    from datetime import date

    idade = date.today().year - nasc
    if idade <= 15:
        return f'Com {idade} anos o voto é NEGADO'
    elif idade >= 65 or (idade >= 16 and idade < 18):
        return f'Com {idade} anos o voto é OPCIONAL'
    else:
        return f'Com {idade} anos o voto é OBRIGATÓRIO'



ano_nasc = int(input("Digite o ano de seu nascimento: "))
resp = voto(ano_nasc)
print(resp)