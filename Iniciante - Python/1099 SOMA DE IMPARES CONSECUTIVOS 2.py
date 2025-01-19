# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. 
# Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma 
# de todos os ímpares existentes entre X e Y.

# Entrada
# A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que 
# vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

# Saída
# # Imprima a soma de todos valores ímpares entre X e Y.
'''
7                   
4 5                 0
13 10               11
6 4                 5
3 3                 0
3 5                 0
3 4                 0
3 8                 12
'''

n_entr = int(input())
list_d = []
for i in range(n_entr):
    a, b = map(int, input() .split(' '))
    list_d.append([a, b])

for lista in list_d:
    x = max(lista)
    y = min(lista)

    def numero_impa(x, y):
        soma = []
        if (x - 1) != y and y % 2 == 0:
            y += 1
            for impar in range(y , x, 2):
                soma.append(impar)
        elif y != x and y % 2 != 0 and y +2 != x:
            for impar in range((y+2) , x, 2):
                soma.append(impar)
        if soma is None:
            print('0')
        else:
            print(sum(soma))

    numero_impa(x, y)
