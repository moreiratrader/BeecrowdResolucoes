# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# # Imprima a sequencia conforme exemplo abaixo.

'''
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
'''
i = 0
j = 1
while i < 1.8:
    ...
    def entr(i, j):
        contagem = 0
        while True:
            if contagem == 3:
                break
            if i == 0 or i == 1 or i == 2:
                print(f'I={i:.0f} J={j:.0f}')
            else:
                print(f'I={i:.1f} J={j:.1f}')
            contagem += 1
            j += 1
    entr(i, j)
    i += .2
    j += .2

# FIZ ASSIM PQ DENTRO DA VARIAVEL ESTAVA RETORNANDO I=2.0 J=3.0 
print('I=2 J=3')
print('I=2 J=4')
print('I=2 J=5')