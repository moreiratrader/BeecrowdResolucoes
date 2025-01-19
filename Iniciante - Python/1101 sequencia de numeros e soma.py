# Leia um conjunto não determinado de pares de valores M e N 
# (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, 
# mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre 
# eles (incluindo o N e M).

# Entrada
# O arquivo de entrada contém um número não determinado de valores M e N. 
# A última linha de entrada vai conter um número nulo ou negativo.

# Saída
# Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, 
# conforme exemplo abaixo.
'''
5 2             2 3 4 5 Sum=14
6 3             3 4 5 6 Sum=18
5 0             
'''

while  True:
    a1, a2 = map(int, input().split(' '))
    soma = 0
    mesma_linha = ''

    if a1 == 0 or a2 == 0:
        break
    if a1 > a2:
        for numero in range(a2, (a1 + 1)):
            soma += numero
            mesma_linha += str(numero) + ' '
    else:
        for numero in range(a1, (a2 + 1)):
            soma += numero
            mesma_linha += str(numero) + ' '
    if soma != 0 or soma < 0:
        print(f'{mesma_linha}Sum={soma}')
    else:
        break