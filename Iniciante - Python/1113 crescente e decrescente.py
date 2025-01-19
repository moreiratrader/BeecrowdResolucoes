# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. 
# Escreva para cada X e Y uma mensagem que indique se estes valores foram 
# digitados em ordem crescente ou decrescente.

# Entrada
# A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. 
# A leitura deve ser encerrada ao ser fornecido valores iguais para X e Y.

# Saída
# Para cada caso de teste imprima “Crescente”, caso os valores tenham sido 
# digitados na ordem crescente, caso contrário imprima a mensagem “Decrescente”.
'''
5 4                 Decrescente
7 2                 Decrescente
3 8                 Crescente
2 2
'''
while True:
    x, y = map(int, input() .split())

    if x == y:
        break
    
    if x > y:
        print('Decrescente')
    else:
        print('Crescente')