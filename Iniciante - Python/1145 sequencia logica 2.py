'''
Escreva um programa que leia dois valores X e Y. A seguir, mostre uma 
sequência de 1 até Y, passando para a próxima linha a cada X números.

Entrada
O arquivo de entrada contém dois valores inteiros, (1 < X < 20) 
e (X < Y < 100000).

Saída
Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco
 entre cada número, conforme exemplo abaixo. Não deve haver espaço em branco 
 após o último valor da linha.

Exemplo de Entrada	Exemplo de Saída
3 99                    1 2 3
                        4 5 6
                        7 8 9
                        10 11 12
                        ...
                        97 98 99
'''
a, b = map(int, input() .split())
x = min(a, b)
y = max(a, b)

def contagem(star, stop):
    sequencia = star
    espaco = ' '
    tres_numeros = ''
    for numero in range(1, stop + 1):
        if sequencia > 1:
            sequencia -= 1
            tres_numeros += str(numero) + espaco
        else:
            sequencia = star
            tres_numeros += str(numero)
            print(tres_numeros)
            tres_numeros = ''

contagem (x, y)