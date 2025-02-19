'''
Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada,
 um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. 
 Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, 
 conforme for o caso. A imagem abaixo ilustra o caso da entrada do valor 5 para a coluna da matriz, 
 demonstrando os elementos que deverão ser considerados na operação.


Entrada
A primeira linha de entrada contem um número C (0 ≤ C ≤ 11) indicando a coluna que será considerada para operação. 
A segunda linha de entrada contém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média) 
que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
5                       12.6
S
0.0
-3.5
2.5
4.1
...
'''
headquarters = int(input())
sum_average = input().upper()
lines = []
line_select = []
for _ in range(12):
    line = []
    for i in range(12):
        l = float(input())
        line.append(l)
    lines.append(line)

for list_ in lines:
    for i, l_ in enumerate(list_):
        if i == headquarters:
            line_select.append(l_)
            break
if sum_average == 'M':
    complete = sum(line_select) / 12
else:
    complete = sum(line_select)

print(f'{complete:.1f}')
