'''
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de inteiros, 
e construa a matriz de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. 
O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. 
Os valores das matrizes devem ser formatados em um campo de tamanho T justificados à direita e separados por espaço, 
onde T é igual ao número de dígitos do maior número da matriz.
Após o último caractere de cada linha da matriz não deve haver espaços em branco. 
Após a impressão de cada matriz deve ser deixada uma linha em branco.

Exemplo de Entrada	Exemplo de Saída
1                       1
2
3                       1 2
4                       2 4
5
0                       1  2  4
                        2  4  8
                        4  8 16

                        1  2  4  8
                        2  4  8 16
                        4  8 16 32
                        8 16 32 64

                        1   2   4   8  16
                        2   4   8  16  32
                        4   8  16  32  64
                        8  16  32  64 128
                        16  32  64 128 256
'''

def contr_matrix(n):
    #     matriz = [[2 ** (i + j) for j in range(n)] for i in range(n)]
    #     return matriz
    matrix = []
    for i in range(0, n):
        row = []
        for j in range(0, n):
            number = 2** (i + j)
            row.append(number)
        matrix.append(row)
    return matrix

def format_matrix(matrix):
    matrix_print = []
    big_num = matrix[-1][-1]
    t = len(str(big_num))
    for row in matrix:
        matrix_print.append(' '.join(f'{num:>{t}}' for num in row))

    return '\n'.join(matrix_print)
        
while True:
    n = int(input())
    if n == 0:
        break
    else:
        craft_matrix = contr_matrix(n)
        print(format_matrix(craft_matrix))
        print()

