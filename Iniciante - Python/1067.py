# Leia um valor inteiro X (1 <= X <= 1000). 
# Em seguida mostre os ímpares de 1 até X, um valor por linha, 
# inclusive o X, se for o caso.

# Entrada
# O arquivo de entrada contém 1 valor inteiro qualquer.

# Saída
# Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.
# 8                               1
                                # 3
                                # 5
                                # 7

x = int(input())
x1 = x+1
for numero in range(1, x1, 2):
    print(numero)