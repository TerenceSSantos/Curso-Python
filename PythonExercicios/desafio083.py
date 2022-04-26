#   Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
#   analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

print('=' * 60)
expressao = str(input('Digite a expressão: '))
aberto = fechado = 0
for i in range(0, len(expressao)):
    if expressao[i] == '(':
        aberto += 1
    elif expressao[i] == ')':
        fechado += 1
if aberto == fechado:
    print('Sua expressão está válida!')
else:
    print('Está expressão NÃO é Válida!')