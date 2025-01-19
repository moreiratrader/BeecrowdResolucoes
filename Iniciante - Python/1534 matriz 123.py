'''
Entrada
A entrada contém vários casos de teste e termina com EOF. 
Cada caso de teste é composto por um único inteiro N (3 ≤ N < 70), que determina o tamanho 
(linhas e colunas) de uma matriz que deve ser impressa.

Saída
Para cada N lido, apresente a saída conforme o exemplo fornecido.

Exemplo de Entrada	Exemplo de Saída
4                       1332
7                       3123
                        3213
                        2331
                        1333332
                        3133323
                        3313233
                        3332333
                        3323133
                        3233313
                        2333331
''' 
one = 1
tw = 2
th = 3
save_next_1 = 0

while True:
    try:
        x = int(input())
    except:
        break

    row = []
    for colunm in range(0, x):
         
        if colunm == 0 and len(row) == 0:
            row.append(one)
            for number in range(0, x-2):
                row.append(th)
            row.append(tw)
        else:
            try:
                check_2 = row.index(2)
                check_1 = row.index(1)
            except ValueError:
                row.insert(save_next_1, one)
                row.pop()

            if check_1 + 1 != check_2 - 1 and x % 2 == 0:         
                index_2 = row.index(2)
                number = row.pop(index_2)
                row.insert(index_2 - 1, number)
                if check_1 + 1 != check_2:
                    index_1 = row.index(1)
                    number = row.pop(index_1)
                    row.insert(index_1 + 1, number)
            else:

                if check_1 + 1 != check_2 -1:
                    index_1 = row.index(1)
                    number = row.pop(index_1)
                    row.insert(index_1 + 1, number)
                    index_2 = row.index(2)
                    number = row.pop(index_2)
                    row.insert(index_2 - 1, number)
                else:
                    save_next_1 = check_2 - 1
                    without_1 = row.pop(check_1)
                    row.append(th)

        result = ''.join(map(str, row))
        print(result)
