'''
Faça um programa que leia um valor e apresente o número de Fibonacci 
correspondente a este valor lido. Lembre que os 2 primeiros elementos 
da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 
anteriores a ele. Todos os valores de Fibonacci calculados neste 
problema devem caber em um inteiro de 64 bits sem sinal.

Entrada
A primeira linha da entrada contém um inteiro T, indicando o número de 
casos de teste. Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), 
correspondente ao N-esimo termo da série de Fibonacci.

Saída
Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", 
onde X é o N-ésimo termo da série de Fibonacci.

Exemplo de Entrada	Exemplo de Saída
3
0                   Fib(0) = 0
4                   Fib(4) = 3
2                   Fib(2) = 1
'''
entry = int(input())


f1 = 0
f2 = 1
seq = [0, 1]
for _ in range(61):
    f = f1 + f2
    f1 = f2
    f2 = f
    seq.append(f)

for i in  range(entry):
    n = int(input())
    print(f'Fib({n}) = {seq[n]}')