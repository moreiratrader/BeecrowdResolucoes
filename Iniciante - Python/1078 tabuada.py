# Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
# 1 x N = N      2 x N = 2N        ...       10 x N = 10N

# Entrada
# A entrada contém um valor inteiro N (2 < N < 1000).

# Saída
# Imprima a tabuada de N, conforme o exemplo fornecido.

# 140

n = int(input())

for numero in range(1, 11):
    tabuada = numero * n
    print(f'{numero} x {n} = {tabuada}')