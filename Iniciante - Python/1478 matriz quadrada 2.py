''''
Entrada
A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. 
O final da entrada é marcado por um valor de ordem igual a zero (0).

Saída
Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. 
(os valores das matrizes devem ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço.
 Após o último caractere de cada linha da matriz não deve haver espaços em branco. 
 Após a impressão de cada matriz deve ser deixada uma linha em branco.

Exemplo de Entrada	Exemplo de Saída
1                       1
2 
3                       1   2
4                       2   1
5
0   	                1   2   3
                        2   1   2
                        3   2   1

                        1   2   3   4
                        2   1   2   3
                        3   2   1   2
                        4   3   2   1

                        1   2   3   4   5
                        2   1   2   3   4
                        3   2   1   2   3
                        4   3   2   1   2
                        5   4   3   2   1
'''
while True:
    x = int(input())
    if x == 0:
        break
    for i, coluna in enumerate(range(0, x)):
        coluna += 1
        last= 0
        for count, linha in enumerate(range(0, x)):
            if i == 0 :
                linha += 1
                degree = linha
            elif linha == 0:
                degree = coluna
            else:
                if coluna - 1 == 1 and last != 1: #and equal_one is not True:
                    coluna -= 1
                    degree = coluna
                elif coluna - 1 > 1:
                    coluna -= 1
                    degree = coluna
                else:
                    last += 1
                    degree = last         
           
            print(f'{degree:3}', end="")
            if count < x - 1:
                print(end=' ')

            last = degree

        print()
    print()