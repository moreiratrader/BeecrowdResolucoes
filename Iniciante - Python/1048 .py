# A empresa ABC resolveu conceder um aumento de salários a seus funcionários 
# de acordo com a tabela abaixo:

# Salário	Percentual de Reajuste
# 0 - 400.00                    15%
# 400.01 - 800.00               12%
# 800.01 - 1200.00              10%
# 1200.01 - 2000.00             7%
# Acima de 2000.00              4%

# Leia o salário do funcionário e calcule e mostre o novo salário,
#  bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

# Saída
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste 
# (ambos devem ser apresentados com 2 casas decimais) 
# e o percentual de reajuste ganho, conforme exemplo abaixo.
# 400.00            Novo salario: 460.00
#                   Reajuste ganho: 60.00
#                   Em percentual: 15 %

# 800.01            Novo salario: 880.01
#                   Reajuste ganho: 80.00
#                   Em percentual: 10 %


# 2000.00           Novo salario: 2140.00
#                   Reajuste ganho: 140.00
#                   Em percentual: 7 %

bruto = float(input())

aumento = (0.15, 0.12, 0.10, 0.07, 0.04)
ajuste = 0

if bruto <= 400:
    ajuste = bruto * aumento[0]
    print(f'Novo salario: {bruto + ajuste:.2f}')
    print(f'Reajuste ganho: {ajuste:.2f}')
    print(f'Em percentual: 15 %')
if 400 < bruto <= 800:
    ajuste = bruto * aumento[1]
    print(f'Novo salario: {bruto + ajuste:.2f}')
    print(f'Reajuste ganho: {ajuste:.2f}')
    print(f'Em percentual: 12 %')

if 800 < bruto <= 1200:
    ajuste = bruto * aumento[2]
    print(f'Novo salario: {bruto + ajuste:.2f}')
    print(f'Reajuste ganho: {ajuste:.2f}')
    print(f'Em percentual: 10 %')

if 1200 < bruto <= 2000:
    ajuste = bruto * aumento[3]
    print(f'Novo salario: {bruto + ajuste:.2f}')
    print(f'Reajuste ganho: {ajuste:.2f}')
    print(f'Em percentual: 7 %')

if  bruto > 2000:
    ajuste = bruto * aumento[4]
    print(f'Novo salario: {bruto + ajuste:.2f}')
    print(f'Reajuste ganho: {ajuste:.2f}')
    print(f'Em percentual: 4 %')