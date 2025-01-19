'''
Os dados armazenados no computador estão em binário. Uma forma econômica de 
ver estes números é usar a base 16 (hexadecimal).

Sua tarefa consiste em escrever um programa que, dado um número natural na 
base 10, mostre sua representação em hexadecimal.

Entrada
A entrada é um número inteiro positivo V na base 10 (1 ≤ V ≤ 2 x 109).

Saída
A saída é o mesmo número V na base 16 em uma única linha 
(não esqueça do caractere de fim-de-linha). Use letras maiúsculas, 
conforme os exemplos.

Exemplos de Entrada	Exemplos de Saída
10                      A

15                      F

16                      10

31                      1F

65535                   FFFF
'''
def decToHexa(n):
    hexaDeciNum = ['0'] * 100
    i = 0
    while (n != 0):
        temp = 0
        temp = n % 16
        if (temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        n = int(n / 16)
    j = i - 1
    while (j >= 0):
        print((hexaDeciNum[j]), end="")
        j = j - 1
n = int(input())
decToHexa(n)
print()