# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, 
# quantos valores digitados foram ímpares, quantos valores digitados foram positivos
#  e quantos valores digitados foram negativos.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, 
# não esquecendo o final de linha após cada uma.

# -5                    3 valor(es) par(es)
# 0                     2 valor(es) impar(es)
# -3                    1 valor(es) positivo(s)
# -4                    3 valor(es) negativo(s)
# 12

lista = []
par = 0
impar = 0
positivo = 0
negativo = 0

for entr in range(5):
    entr = int(input())
    lista.append(entr)

for numero in lista:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
        
    if numero > 0:
        positivo += 1

    elif numero < 0:
        negativo += 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
