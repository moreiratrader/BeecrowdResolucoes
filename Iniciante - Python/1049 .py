# Neste problema, você deverá ler 3 palavras que definem o tipo de animal 
# possível segundo o esquema abaixo, da esquerda para a direita.  
# Em seguida conclua qual dos animais seguintes foi escolhido, 
# através das três palavras fornecidas.

tipo = input()
se_alimenta = input()
animal = input()
dicionarios = {
    'vertebrado' : {
            'ave' : {'carnivoro' :'aguia',
                'onivoro' : 'pomba'},
            'mamifero' : {'onivoro' : 'homem',
                      'herbivoro' : 'vaca'},     
    },
    'invertebrado' : {
        'inseto' : {'hematofago' : 'pulga',
                    'herbivoro' : 'lagarta'},
        'anelideo' : {'hematofago' : 'sanguessuga',
                    'onivoro' : 'minhoca'},
    },
}
# print(vertebrado['ave']['carnivoro'])
print(dicionarios[f'{tipo}'][f'{se_alimenta}'][f'{animal}'])