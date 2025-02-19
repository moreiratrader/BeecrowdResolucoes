'''
Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos 
números que não são múltiplos de 13 entre X e Y, incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente 
em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores 
lidos na entrada, inclusive ambos se for o caso.

100         13954
200
'''

a = int(input())
b = int(input())
x = min(a, b)
y = max(a, b)

def multiplos(x, y):
    nao_multiplos = 0
    for numero in range(x,(y+1)):
        if numero % 13 != 0:
            nao_multiplos += numero
    return nao_multiplos

print(multiplos(x, y))