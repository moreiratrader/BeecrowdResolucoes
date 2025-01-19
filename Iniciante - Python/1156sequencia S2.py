'''
Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Entrada
Não há nenhuma entrada neste problema.

Saída
A saída contém um valor correspondente ao valor de S.
O valor deve ser impresso com dois dígitos após o ponto decimal.
'''

s = 1
cima = []
baixo = [2 , 4, 8]

for numero in range(3, 40, 2):
    cima.append(numero)

while len(cima) != len(baixo):
    multi = 2
    calculo = multi * baixo[-1]
    baixo.append(calculo)

for c, b in zip(cima, baixo):
    s += c/b

print(f'{s:.2f}')