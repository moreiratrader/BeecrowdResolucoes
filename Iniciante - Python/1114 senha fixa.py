# Escreva um programa que repita a leitura de uma senha até que ela seja válida. 
# Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". 
# Quando a senha for informada corretamente deve ser impressa a 
# mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha 
# correta é o valor 2002. 

# Entrada
# A entrada é composta por vários casos de testes contendo valores inteiros.

# Saída
# Para cada valor lido mostre a mensagem correspondente à descrição do problema.
'''
2200            Senha Invalida
1020            Senha Invalida
2022            Senha Invalida
2002            Acesso Permitido
'''

senha_correta = '2002'
senha_ok = False

while senha_ok is False:
    senha_digitada = input()

    if senha_digitada in senha_correta:
        print('Acesso Permitido')
        senha_ok = True
    else:
        print('Senha Invalida')
