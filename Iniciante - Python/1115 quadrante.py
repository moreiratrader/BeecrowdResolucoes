# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de 
# pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. 
# O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA 
# (nesta situação sem escrever mensagem alguma).

# Entrada
# A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

# Saída
# Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a 
# coordenada lida, conforme o exemplo.

'''
2 2                     primeiro
3 -2                    quarto
-8 -1                   terceiro
-7 1                    segundo
0 2
'''

while True:
    y, x = map(int, input() .split())

    if y == 0 or y == 0:
        break
    if y > 0 and x > 0:
        print('primeiro')
    elif y > 0 and x < 0:
        print('quarto')
    elif y < 0 and x > 0:
        print('segundo')
    else:
        print('terceiro')