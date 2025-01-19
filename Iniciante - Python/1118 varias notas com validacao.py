'''
Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. 
Calcule e imprima a média semestral. O programa só deverá aceitar notas válidas 
(uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada 
separadamente.

No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, 
solicitando ao usuário que informe um código (1 ou 2) indicando se ele deseja ou não 
executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o 
código 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, 
caso contrário o programa deve ser encerrado.

Entrada
O arquivo de entrada contém vários valores reais, positivos ou negativos. 
Quando forem lidas duas notas válidas, deve ser lido um valor inteiro X . 
O programa deve parar quando o valor lido para este X for igual a 2.

Saída
Se uma nota inválida for lida, deve ser impressa a mensagem “nota invalida”. 
Quando duas notas válidas forem lidas, deve ser impressa a mensagem “media = ” 
seguido do valor do cálculo.

Antes da leitura de X deve ser impressa a mensagem "novo calculo (1-sim 2-nao)" e 
esta mensagem deve ser apresentada novamente se o valor da entrada padrão para X for menor
do que 1 ou maior do que 2, conforme o exemplo abaixo.

A média deve ser impressa com dois dígitos após o ponto decimal.
-3.5            nota invalida
3.5             nota invalida
11.0            media = 6.75
10.0            novo calculo (1-sim 2-nao)
4               novo calculo (1-sim 2-nao)
1               media = 8.50
8.0             novo calculo (1-sim 2-nao)
9.0
2
'''
def ler_nota():
    """Lê uma nota válida no intervalo [0,10]."""
    while True:
        nota = float(input())
        if 0 <= nota <= 10:
            return nota
        else:
            print("nota invalida")

def novo_calculo():
    """Pergunta ao usuário se deseja realizar um novo cálculo."""
    while True:
        print("novo calculo (1-sim 2-nao)")
        escolha = int(input())
        if escolha in [1, 2]:
            return escolha
        else:
            continue  # Volta para a pergunta caso a entrada seja inválida.

while True:
    # Lê as duas notas válidas.
    nota1 = ler_nota()
    nota2 = ler_nota()

    # Calcula e exibe a média.
    media = (nota1 + nota2) / 2
    print(f"media = {media:.2f}")

    # Pergunta se o usuário deseja realizar um novo cálculo.
    if novo_calculo() == 2:
        break  # Encerra o programa.