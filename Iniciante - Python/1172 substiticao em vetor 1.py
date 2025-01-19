'''
Faça um programa que leia um vetor X[10]. Substitua a seguir, 
todos os valores nulos e negativos do vetor X por 1. Em seguida 
mostre o vetor X.

Entrada
A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

Saída
Para cada posição do vetor, escreva "X[i] = x", onde i é a 
posição do vetor e x é o valor armazenado naquela posição.

Exemplo de Entrada	Exemplo de Saída
0                   X[0] = 1
-5                  X[1] = 1
63                  X[2] = 63
0                   X[3] = 1
...                 ...
'''
x = 0
while x < 10:
    entry = int(input())
    if entry <= 0:
        x0 = 1
        print(f'X[{x}] = {x0}')
        x += 1
        continue
    else:
        print(f'X[{x}] = {entry}')
        x += 1
