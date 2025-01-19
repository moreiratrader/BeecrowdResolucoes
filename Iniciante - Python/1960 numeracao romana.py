'''
A ECI (Editio Chronica Incredibilis ou Editora de Crônicas Incríveis) 
é muito tradicional quando se trata de numerar as páginas de seus livros. 
Ela sempre usa a numeração romana para isso. 
E seus livros nunca ultrapassam as 999 páginas pois, quando necessário, 
dividem o livro em volumes.

Você deve escrever um programa que, dado um número arábico, mostra seu 
equivalente na numeração romana.

Lembre que I representa 1, V é 5, X é 10, L é 50, C é 100, D é 500 e M 
representa 1000.

Entrada
A entrada é um número inteiro positivo N (0 < N < 1000).

Saída
A saída é o número N escrito na numeração romana em uma única linha. 
Use sempre letras maiúsculas.

Exemplos de Entrada	Exemplos de Saída
666                     DCLXVI

83                      LXXXIII

999                     CMXCIX
'''

num = int(input())
roman_dict = { 
    1000 : 'M', 900 : 'CM', 500 : 'D', 400 : 'CD', 100 : 'C',
    90 : 'XC', 50 : 'L', 40 : 'XL', 10 : 'X',
    9 : 'IX', 5 : 'V', 4 : 'IV', 1 : 'I',
}
roman_num = ""
for value in roman_dict:
    while value <= num:
            roman_num += roman_dict[value]
            num -= value
    if num == 0:
          break

print(roman_num)