# Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, 
# de 1 até N, inclusive N, se for o caso.

# Entrada
# A entrada contém um valor inteiro N (5 < N < 2000).

# Saída
# Imprima o quadrado de cada um dos valores pares, de 1 até N, conforme o exemplo abaixo.

# Tome cuidado! Algumas linguagens tem por padrão apresentarem como saída 1e+006 ao invés 
# de 1000000 o que ocasionará resposta errada. Neste caso, configure a precisão adequadamente 
# para que isso não ocorra.

# 6             2^2 = 4
#               4^2 = 16
#               6^2 = 36

n = int(input())

if n % 2 == 0:
    n += 1
    for numero in range(2, n, 2):
        exponenciacao = numero ** 2
        print(f'{numero}^2 = {exponenciacao}')
else:
    for numero in range(2, n , 2):
        exponenciacao = numero ** 2
        print(f'{numero}^2 = {exponenciacao}')

