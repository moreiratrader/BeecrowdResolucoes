'''
A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma 
estatística do resultado de vários GRENAIS. Escreva um programa para ler o número de gols 
marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem 
"Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo 
deve ser executado novamente solicitando o número de gols marcados pelos times em uma 
nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS 
(ou "Nao houve vencedor", caso termine empatado).

Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo 
Inter e pelo Grêmio respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente
 à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". 
Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição
 apresentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o 
 exemplo abaixo.

3 2                 Novo grenal (1-sim 2-nao)
1                   Novo grenal (1-sim 2-nao)
2 3                 Novo grenal (1-sim 2-nao)
1                   3 grenais
3 1                 Inter:2
2                   Gremio:1
                    Empates:0
                    Inter venceu mais
'''

qtd_inter = 0
qtd_gremio = 0
qtd_empate = 0

def qtd_grenal():
    inter, gremio = map(int, input().split())
    return inter, gremio
def novo_grenal():
    while True:
        print("Novo grenal (1-sim 2-nao)")
        escolha = int(input())
        if escolha in [1, 2]:
            return escolha
        else:
            continue
def venceu(inter, gremio, empate):
    if inter > gremio:
        return 'Inter'
    elif inter < gremio:
        return 'Gremio'
    else: 
        return 'Empate'

while True:
    inter, gremio = qtd_grenal()
    if inter > gremio:
        qtd_inter += 1
    elif inter < gremio:
        qtd_gremio += 1
    else:
        qtd_empate += 1
    if novo_grenal() == 2:
        print(f'{qtd_inter + qtd_gremio + qtd_empate} grenais')
        print(f'Inter:{qtd_inter}')
        print(f'Gremio:{qtd_gremio}')
        print(f'Empates:{qtd_empate}')
        print(f'{venceu(qtd_inter, qtd_gremio, qtd_empate)} venceu mais')
        break

    