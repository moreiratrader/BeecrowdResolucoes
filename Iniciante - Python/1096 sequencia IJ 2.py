# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo
'''
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
'''
j = 7
i = 1
while i <= 9:
    print(f'I={i} J={j}')

    if j == 5:
        j += 3
        i += 2
    if i == 9 and j == 5:
        break
    j -= 1