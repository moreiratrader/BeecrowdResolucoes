'''
Um Posto de combustíveis deseja determinar qual de seus produtos tem a 
preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível 
abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). 
Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser 
solicitado um novo código (até que seja válido). O programa será encerrado 
quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que 
abasteceram cada tipo de combustível, conforme exemplo.

Exemplo de Entrada	Exemplo de Saída
8                   MUITO OBRIGADO
1                   Alcool: 1
7                   Gasolina: 2
2                   Diesel: 0
2
4
'''
qtd_alcool = 0
qtd_gasolina = 0
qtd_diesel = 0

def entr():
    while True:
        tipo = int(input())
        if tipo >= 1 and tipo <=  4:
            return tipo

while True:
    tipo = entr()
    if tipo == 1:
        qtd_alcool += 1
    elif tipo == 2:
        qtd_gasolina += 1
    elif tipo == 3:
        qtd_diesel += 1
    else:
        print(f"MUITO OBRIGADO\nAlcool: {qtd_alcool}\nGasolina: {qtd_gasolina}")
        print(f'Diesel: {qtd_diesel}')
        break
