# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo.
# A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” 
# 7 8 9 10        O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
# 7 7 7 7         O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)
# 7 10 8 9        O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)
# fui ver uma solução, a minha logica estava ficando muito extensa e complexa.
hora_i, minuto_i, hora_f, minuto_f = map(int, input().split(' '))

minuto_i += hora_i * 60
minuto_f += hora_f * 60

tempo = minuto_f - minuto_i

if tempo <= 0:
    tempo += 24 * 60

horas = tempo // 60
minutos = tempo % 60

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')