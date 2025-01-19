'''
Escreva um programa que leia 2 valores X e Y e que imprima todos os 
valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não 
necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

Sample Input	Sample Output
10              12
18              13
                17
'''
a = int(input())
b = int(input())
x = min(a, b)
y = max(a, b)
if x <= 2:
    x = 3

for numero in range (x, y):
    resto_d = numero % 5
    if resto_d >= 2 and resto_d <=3:
        print(numero)