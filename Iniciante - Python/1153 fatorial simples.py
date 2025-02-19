'''
Ler um valor N. Calcular e escrever seu respectivo fatorial. 
Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada
A entrada contém um valor inteiro N (0 < N < 13).

Saída
A saída contém um valor inteiro, correspondente ao fatorial de N.

Exemplo de Entrada	Exemplo de Saída
4                       24
'''

def fatorail():
    n = int(input())
    fator = 1

    for numero in range(n, 0, -2):
        fator *= numero * (numero - 1)
    print(fator)

fatorail()
