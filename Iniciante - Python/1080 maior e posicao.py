# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

# Entrada
# O arquivo de entrada contém 100 números inteiros, positivos e distintos.

# Saída
# Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''
2                           34565
113                         4
45
34565
6
...
8
'''
maior = 0
lista = []
posicao = 0
for entr in range(100):
    entr= int(input())
    lista.append(entr)

maior = max(lista)
posicao = lista.index(maior)
posicao += 1
print(maior)
print(posicao)




