'''
Escreva um programa que leia um valor inteiro N (1 < N < 1000). 
Este N é a quantidade de linhas de saída que serão apresentadas na execução 
do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
5                       1 1 1
                        2 4 8
                        3 9 27
                        4 16 64
                        5 25 125
primeira coluna ao quadrado, mult a 1 pela 2
'''
soma = [1]
cubo = [1]
multiplicacao = [1]
def quadrado(numero1):
    numero1 *= numero1
    return numero1

def multiplica(numero1, numero2):
    multi = numero1 * numero2
    return multi

n_repeti = int(input())

for numero in range(2, n_repeti + 1):
    soma.append(numero)

for numero in soma[1::]:
    quad = quadrado(numero)
    cubo.append(quad)

for n1, n2 in zip(soma[1::], cubo[1::]):
    mul = multiplica(n1,n2)
    multiplicacao.append(mul)

for n1, n2, n3 in zip(soma, cubo, multiplicacao):
    print(n1, n2, n3)