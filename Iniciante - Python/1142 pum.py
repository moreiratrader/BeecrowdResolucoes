'''
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de 
linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
7                       1 2 3 PUM
                        5 6 7 PUM
                        9 10 11 PUM
                        13 14 15 PUM
                        17 18 19 PUM
                        21 22 23 PUM
                        25 26 27 PUM
'''
quantidade = int(input())
def repeticoes (repeti):
    x = 1
    y = 3
    linhas = repeti
    while linhas != 0:
        espaco = ' '
        mostra = ''
        for numero in range(x, (y+1)):
            mostra += str(numero) + espaco
        print(f'{mostra}PUM')
        x += 4
        y += 4
        linhas -= 1
repeticoes(quantidade)