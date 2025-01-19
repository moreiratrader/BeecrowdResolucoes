'''
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da 
diagonal principal da matriz, conforme ilustrado abaixo (área verde).

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), 
indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. 
Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
S                   12.6
1.0
0.0
-3.5
2.5
4.1
...
'''

sum_or_average = input().upper()
all_lines = []
line_select = []
headquarters = 0

for _ in range(12):
    generator = []
    for i in range(12):
        l = float(input())
        generator.append(l)
    all_lines.append(generator)

def num_select(list, headquarters):
    adc = 0
    for i, number in enumerate(list):
        if i > headquarters:
            adc += number

    return adc 

for list_ in all_lines:
    line_select.append(num_select(list_, headquarters))
    headquarters += 1

if sum_or_average == 'M':
    complete = sum(line_select) / 66
    
else:
    complete = sum(line_select)

print(f'{complete:.1f}')
