# Leia um valor inteiro X. 
# Em seguida apresente os 6 valores ímpares consecutivos a partir de X,
# um valor por linha, inclusive o X ser for o caso.

# Entrada
# A entrada será um valor inteiro positivo.

# Saída
# A saída será uma sequência de seis números ímpare
# 8           9
#             11
#             13
#             15
#             17
#             19

x = int(input())
proximos_seis = x + 13
impresos = 0
if x % 2 == 0:
    x += 1
    for numero in range(x, proximos_seis, 2):
        
        print(numero)
else:
    for numero in range(x, proximos_seis, 2):
        if impresos != 6:
            impresos += 1
            print(numero)