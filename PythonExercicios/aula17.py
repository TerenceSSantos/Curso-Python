#   AULA SOBRE LISTAS

num = [2, 5, 9, 1]  # Listas utilizam colchetes
print('='*30)
print('Mostrando a lista:', num)
num[2] = 3  # incluindo o valor 3 na posição 2 da lista
print('='*30)
print('num[2]. Inclusão do valor 3 na posição 2 da lista:', num)
num.append(7)   # incluindo o valor 7 na última posição
print('='*30)
print('num.append. Foi incluído o 7 na última posição', num)
print('='*30)
num.sort()  # ordenando a lista
print('='*30)
print('num.sort(). Foi posto em ordem', num)
num.sort(reverse=True)  # ordem decrescente
print('='*30)
print('num.sort(reverse=True). Ordem decrescente:', num)
print('='*30)
print(f'len(num). Essa lista tem {len(num)} elementos.')
num.insert(2, 0)    # Inserindo o 0 na posição 2
print('='*30)
print('num.insert(2, 0). Inserindo o 0 na posição 2', num)
num.pop()   # elimina o último valor
print('='*30)
print('num.pop() elimina o último valor', num)
num.pop(2)  # elimina o valor da posição 2
print('='*30)
print('num.pop(2). Elimina o valor da posição 2', num)
num.insert(2, 2)    # inserindo 2 na posição 2
print('='*30)
print('num.insert(2, 2). Inserindo o 2 na posição 2', num)
num.remove(2)   # excluir o valor 2 da lista. Excluirá o primeiro que encontrar
print('='*30)
print('num.remove(2). Excluir o primeiro valor 2 que encontrar', num)
valores = []    # ou valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print('='*30)
print(valores)
for v in valores:
    print(f'{v}...', end='')
print('='*30)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

a = [2, 3, 4, 7]
b = a
b[2] = 8    # lista "a" também será modificada. Característica das listas em Python
print('lista a:', a)
print('Lista b:', b)
b = a[:] # desta forma b recebe todos os itens de "a"
b[3] = 9
print('lista a:', a)
print('Lista b:', b)