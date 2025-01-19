# Leia a hora inicial e a hora final de um jogo. 
# A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e 
# terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
# 16 2       0 0       2 16
# comeco, fim = map(int, input() .split(' '))
# total = 0

# if 0< comeco > 12 and fim > 0:
#     for comeco in range(comeco,24):
#         total += 1

#     for continua in range(0, fim):
#         total+=1
        
# else:
#     for comeco in range(comeco, fim):
#         total += 1

# if comeco == fim:
#     print('O JOGO DUROU 24 HORA(S)')

# if comeco > 0 and fim == comeco:
#     print('O JOGO DUROU 1 HORA(S)')
   
# if total != 0:
#     print(f'O JOGO DUROU {total} HORA(S)')

comeco_jogo, fim_jogo = map(int, input() .split(' '))

horas = 0

if comeco_jogo < fim_jogo:
    for i in range(comeco_jogo, fim_jogo, 1):
        horas += 1
    print(f'O JOGO DUROU {horas} HORA(S)')

if comeco_jogo > fim_jogo:
    for i in range(comeco_jogo, 24):
        horas += 1

    for i in range(0, fim_jogo):
        horas += 1
    print(f'O JOGO DUROU {horas} HORA(S)')

if comeco_jogo == fim_jogo:
    print('O JOGO DUROU 24 HORA(S)')