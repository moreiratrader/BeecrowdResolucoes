# Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
# Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, 
# com um dígito após o ponto decimal.

# Entrada
# A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante.
# ] Pelo menos um destes números será positivo.

# Saída
# O primeiro valor de saída é a quantidade de valores positivos.
# A próxima linha deve mostrar a média dos valores positivos digitados.
# 7                             4 valores positivos
# -5                             7.4   
# 6
# -3.4
# 4.6
# 12

lista = []
lista_positiva = []
soma = 0
for entr in range(6):
    entr = float(input())
    lista.append(entr)
for i, numero in enumerate(lista):
    if numero > 0:
            lista_positiva.append(numero)
            soma += numero
            
print(f'{len(lista_positiva)} valores positivos')
print(f'{(soma/len(lista_positiva)):.1f}')
