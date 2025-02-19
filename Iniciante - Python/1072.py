# Leia um valor inteiro N. Este valor será a quantidade de valores 
# inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e 
# quantos estão fora do intervalo, mostrando essas informações.

# Entrada
# A primeira linha da entrada contém um valor inteiro N (N < 10000), 
# que indica o número de casos de teste.
# Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

# Saída
# Para cada caso, imprima quantos números estão dentro (in) e quantos
#  valores estão fora (out) do intervalo.
# 4                 2 in
# 14                2 out
# 123
# 10
# -25
n = int(input())
lista = []
dentro = 0
fora = 0
for add in range(n):
    add = int(input())
    lista.append(add)

for numero in lista:
    if 10 <= numero and 20 >= numero:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} in')
print(f'{fora} out')
