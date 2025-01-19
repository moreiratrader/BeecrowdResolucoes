'''
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, 
e construa a matriz de acordo com o exemplo abaixo.

Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. 
O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. 
Os valores das matrizes devem ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. 
Após o último caractere de cada linha da matriz não deve haver espaços em branco. 
Após a impressão de cada matriz deve ser deixada uma linha em branco.

Exemplo de Entrada	Exemplo de Saída
1                       1
2                   
3                       1   1
4                       1   1
5                    
0                       1   1   1 
                        1   2   1
                        1   1   1

                        1   1   1   1
                        1   2   2   1
                        1   2   2   1
                        1   1   1   1

                        1   1   1   1   1
                        1   2   2   2   1
                        1   2   3   2   1
                        1   2   2   2   1
                        1   1   1   1   1
 
'''


while True:
    x = int(input())
    if x == 0:
        break

    for coluna in range(0, x):
        for linha in  range(0, x):
            
            if coluna < x - coluna - 1:
                distL = coluna
            else:
                distL = x-coluna-1

            if linha < x - linha - 1:
                distC = linha
            else:
                distC = x - linha -1

            if distC < distL:
                dist = distC
            else:
                dist = distL

            print(f'{dist+1:3}',end="")
            if linha!= x-1:
                print(end=' ')
            
        print()
    print()