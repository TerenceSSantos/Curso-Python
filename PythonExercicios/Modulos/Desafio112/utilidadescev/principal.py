from Desafio112.utilidadescev import dado, moeda

p = dado.leiaDinheiro(str(input('Digite o preço: R$ ')).strip())
moeda.resumo(p, 80, 35)