# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo.
'''
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
'''
i = 1
j = 7
while i <= 9:
    def entr (i , j):
        ciclos = 0
        while True:
            ciclos += 1
            print(f'I={i} J={j}')
            if ciclos == 3:
                break
            j -= 1
    entr(i, j)
    i += 2
    j += 2

