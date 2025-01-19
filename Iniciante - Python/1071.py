# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos
#  números impares entre eles.

# Entrada
# O arquivo de entrada contém dois valores inteiros.

# Saída
# O programa deve imprimir um valor inteiro. Este valor é a soma dos valores
#  ímpares que estão entre os valores fornecidos na entrada que deverá caber 
# em um inteiro.
# 6                 5
# -5

# 15                13
# 12

# 12                0
# 12
def entr():
    x = int(input())
    y = int (input())

    cont = x - 1
    soma = 0
    while cont > y:
        if cont % 2 != 0:
            soma += cont
        cont -= 1
    print(soma)
    
entr()