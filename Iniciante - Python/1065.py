# Faça um programa que leia 5 valores inteiros. 
# Conte quantos destes valores digitados são pares e mostre esta informação.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, 
# indicando a quantidade de valores pares lidos.
# 7                       3 valores pares
# -5
# 6
# -4
# 12 

lista = []
par = 0

for  entr in range(5):
    entr = int(input())
    lista.append(entr)

for numero in lista:
    par_impar = None
    par_impar = numero % 2

    if par_impar == 0:
        par += 1
        
print(f'{par} valores pares')
