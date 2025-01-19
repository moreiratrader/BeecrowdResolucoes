'''
Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída 
serão apresentadas na execuçãodo programa, seguindo a lógica do exemplo abaixo.
Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

Entrada
O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).

Saída
Imprima a saída conforme o exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
5                       1 1 1
                        1 2 2
                        2 4 8
                        2 5 9
                        3 9 27
                        3 10 28
                        4 16 64
                        4 17 65
                        5 25 125
                        5 26 126
'''
entr = int(input())

def primeira(entrada):
    lista_1 = [1]
    lista_2 = [1, 2]
    for numero in range(1, entrada + 1):
        if lista_1[-1] == numero:
            lista_1.append(numero)
        else:
            lista_1.append(numero)
            lista_1.append(numero)
    for i, numero in enumerate(lista_1):
        if i > 1 and i % 2 == 0:
            multi = numero ** 2
            lista_2.append(multi)

        elif i > 1 and i % 2 != 0:
           repetir =  lista_2[-1]
           lista_2.append(repetir + 1)
    return lista_1, lista_2

coluna1, coluna2 = primeira(entr)
coluna3 = [1, 2]

for i, numero in enumerate(coluna1):
    if i > 1 and i % 2 == 0:
        multiplica =numero * coluna2[i]
        coluna3.append(multiplica)
    elif i > 1:
        ultimo = coluna3[-1]
        coluna3.append(ultimo + 1)

for n1, n2, n3 in zip(coluna1, coluna2, coluna3):
    print(n1, n2, n3)