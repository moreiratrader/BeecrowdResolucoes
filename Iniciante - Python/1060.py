# Faça um programa que leia 6 valores.
# Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
# A seguir, mostre a quantidade de valores positivos digitados.

# Entrada
# Seis valores, negativos e/ou positivos.

# Saída
# Imprima uma mensagem dizendo quantos valores positivos foram lidos.
# 7
# -5
# 6                   4 valores positivos
# -3.4
# 4.6
# 12
list = []
pares = 0
for numero in range(6):
    entr = float(input())
    list.append(entr)
    
for numero in list:
    if numero > 0:
        pares +=1

print(f'{pares} valores positivos')