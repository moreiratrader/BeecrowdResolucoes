# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. 
# Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. 
# Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que
#  o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

# Entrada
# O arquivo de entrada contém um valor inteiro N na primeira linha. 
# Cada N linha a seguir contém um caso de teste com três valores com uma 
# casa decimal cada valor.

# Saída
# Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.
'''
3                               numero de repetições
6.5 4.3 6.2                           5.7
5.1 4.2 8.1                           6.3
8.0 9.0 10.0                          9.3 
'''

# n = int(input())
# list_d = [[6.5, 4.3, 6.2], [5.1, 4.2, 8.1], [8.0, 9.0, 10.0]]
# peso_das_medias = [2, 3, 5]
# valor = 0

# for numero in range(n):
#     n1, n2, n3 = input().split(' ')
#     c1 = float(n1)
#     c2 = float(n2)
#     c3 = float(n3)
#     list_d.append([c1, c2, c3])

# for lista in list_d:
#     for i, number in enumerate(lista):
#         valor += (number * peso_das_medias[i])
#     valor /= 10
#     print(f'{valor:.1f}')

teste = int(input())
contador = 0
while (contador < teste):
    a, b, c = map(float, input() .split())
    media_p = (a * 2 + b * 3 + c * 5) / 10
    print(f'{media_p:.1f}')
    contador += 1