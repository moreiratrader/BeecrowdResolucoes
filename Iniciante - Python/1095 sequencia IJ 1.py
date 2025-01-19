# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo
'''
I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0
'''
j = 60
i = 1
for numero in range(j, -1, -5):
    print(f'I={i} J={numero}')
    i += 3  