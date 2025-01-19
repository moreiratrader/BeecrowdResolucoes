''''
Bem-vindos e bem-vindas à Escola de Inverno da Maratona de Programação 2015 de Erechim! Esperamos sinceramente que vocês 
aprendam muito nestes dias para que tenham muito sucesso nas competições de Programação ainda por vir, mas 
sobretudo esperamos que vocês curtam a Escola, pois quando nos divertimos e temos prazer em estudar e programar, 
o treino deixa de ser um fardo e se torna um hobby. Então, divirtam-se!

O inverno é uma estação maravilhosa, não é mesmo? Todos nós amamos vestir um poncho, participar de uma roda de chimarrão, 
assar pinhões no fogão a lenha… Mas nem todos gostam do inverno, especialmente em lugares onde o inverno costuma 
ser muito cruel. Em Westeros, por exemplo, o humor das pessoas é definido de acordo com as tendências climáticas. 
Com base nas temperaturas dos três últimos dias, as pessoas podem ficar tristes ou felizes, ficando mais propensas a 
fazer guerra ou fazer amor, respectivamente. E, sejamos sinceros, é justamente por causa das cenas de amor e de guerra 
que amamos Game of Thrones!

Se a temperatura desceu do 1º para o 2º dia, mas subiu ou permaneceu constante do 2º para o 3º, as pessoas ficam felizes (primeira figura).
a > b <= c
Se a temperatura subiu do 1º para o 2º dia, mas desceu ou permaneceu constante do 2º para o 3º, as pessoas ficam tristes (segunda figura).
a < b >= c
Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º menos do que subira do 1º para o 2º, as pessoas ficam tristes (terceira figura).
a < b < c and c - b < b -a
Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º no mínimo o tanto que subira do 1º para o 2º, as pessoas ficam felizes (quarta figura).
a < b < c and c - b >= b - a
Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º menos do que descera do 1º para o 2º, as pessoas ficam felizes (quinta figura).
a > b > c and b - c < a - b
Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º no mínimo o tanto que descera do 1º para o 2º, as pessoas ficam tristes (sexta figura).
a > b > c and b -c >= b -a 
Se a temperatura permaneceu constante do 1º para o 2º dia, as pessoas ficam felizes se subiu do 2º para o 3º dia ou tristes caso contrário (respectivamente, sétima e oitava figuras).
a == b and b > c
Entrada
A entrada consiste apenas de três inteiros, A, B e C (-100 ≤ A, B, C ≤ 100), os quais representam respectivamente 
as temperaturas registradas no 1º, no 2º e no 3º dias.

Saída
Imprima uma linha contendo uma carinha feliz ou triste, representando como fica o humor do povo de Westeros de acordo 
com as tendências climáticas.

Exemplos de Entrada	        Exemplos de Saída
20 10 12                    :)          caiu metade e subiu pouco   
10 20 18                        :(      dobrou e caiu pouco
4 16 20                         :(      quadriplicou e subiu 

4 10 20                     :)          subiu mais q o dobro e dobrou
20 10 6                     :)          caiu metade e caiu

20 16 4                         :(      caiu e caiu extremamente forte
10 10 14                    :)          manteve e subiu
10 10 2                         :(      manteve e caiu

'''
def reaction(a, b, c):
    if a > b <= c:
        print(':)')
        return

    elif a < b >= c :
        print(':(')
        return

    elif a < b < c and c - b < b - a:
        print(':(')
        return

    elif a < b < c and c - b >= b - a:
        print(':)')
        return
    
    elif a > b > c and b - c < a - b:
        print(':)')
        return

    elif a > b > c and b -c >= b - a :
        print(':(')
        return

    if a == b and b < c:
        print(':)')
        return

    elif a == b and b > c:
        print(':(')
        return 

    elif b == c and a > b or b == c and a < b:
        print(':)')
        return
    else:
        print(':(')



a, b, c = map(int, input().split())
reaction(a, b, c)

