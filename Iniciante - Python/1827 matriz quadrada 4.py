'''
Neste programa seu trabalho é ler um valor inteiro que será o tamanho da matriz quadrada (largura e altura)
que será preenchida da seguinte forma: a parte externa é preenchida com 0, a parte interna é preenchida com 1, 
a diagonal principal é preenchida com 2, a diagonal secundária é preenchida com 3 e o ponto central contém o valor 4,
conforme os exemplos abaixo.
Obs: o quadrado com '1' sempre começa na posição tamanho/3, tanto na largura quanto quanto na altura. 
A linha e a coluna começam em zero (0).

Entrada
A entrada contém vários casos de teste e termina com EOF (fim de arquivo. 
Cada caso de teste consiste de um valor inteiro ímpar N (5 ≤ N ≤ 101) que é o tamanho da matriz.

Saída
Para cada caso de teste, imprima a matriz correspondente conforme o exemplo abaixo. 
Após cada caso de teste, imprima uma linha em branco.
Exemplo de Saída                Exemplo de Entrada
20003                               5
01110                               11
01410
01110
30002

20000000003
02000000030
00200000300
00011111000
00011111000
00011411000
00011111000
00011111000
00300000200
03000000020
30000000002
'''

def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    # Define the limits of the  innner section
    start = n // 3
    end = n - start
    # Fill the matrix according to the rules
    for i in range(n):
        for j in range(n):
            if i == j:
                if i <= start -1:
                    matrix[i][j] = 2
                elif i >= end:
                    matrix[i][j] = 2
                else:
                    matrix[i][j] = 1

            elif i + j == n -1:
                if i <= start -1:
                    matrix[i][j] = 3
                elif i >= end:
                    matrix[i][j] = 3
                else:
                    matrix[i][j] = 1
            elif start <= i < end and start <= j < end:
                matrix[i][j] = 1
            if i == n // 2 and j == n // 2:
                matrix[i][j] = 4
    return matrix

def print_matrix(matrix):
    # Print the matrix line by line in the required format.
    for row in matrix:
        print(''.join(map(str, row)))
    print()


while True:
    try:
        n = int(input())
        if n % 2 == 1 and 5 <= n <= 101:
            matrix = create_matrix(n)
            print_matrix(matrix)
    except (ValueError, EOFError):
        break            