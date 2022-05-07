#   Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
#   dicionário com as seguintes informações:
#   - Quantidade de notas
#   - A maior nota
#   - A menor nota
#   - A média da turma
#   - A situação (opcional)
#   - Adicione também as docstrings da função

def notas(*num, sit=False):
    """
    => Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    qt_notas = len(num)
    maior_nota = max(num)
    menor_nota = min(num)
    media = 0
    for i in num:
        media += i
    media = media / qt_notas
    dicionario = {'Total': qt_notas, 'Maior': maior_nota, 'Menor': menor_nota, 'Média': media}
    if sit:
        situacao = ''
        if media >= 9:
            situacao = 'ÓTIMA'
        elif media >= 7:
            situacao = 'BOA'
        elif media >= 5:
            situacao = 'RAZOÁVEL'
        elif media >= 2:
            situacao = 'RUIM'
        else:
            situacao = 'PÉSSIMA'
        dicionario['Situação'] = situacao
    return dicionario


        # PROGRAMA PRINCIPAL
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)