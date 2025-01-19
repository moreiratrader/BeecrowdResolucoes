# Pedrinho está organizando um evento em sua Universidade. 
# O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. 
# O problema é que Pedrinho quer calcular o tempo que o evento vai durar, 
# uma vez que ele sabe quando inicia e quando termina o evento.

# Sabendo que o evento pode durar de poucos segundos a vários dias, 
# você deverá ajudar Pedrinho a calcular a duração deste evento.

# Entrada
# Como entrada, na primeira linha vai haver a descrição “Dia”, 
# seguido de um espaço e o dia do mês no qual o evento vai começar.
# Na linha seguinte, será informado o momento no qual o evento vai iniciar,
# no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra
# informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

# Saída
# Na saída, deve ser apresentada a duração do evento, no seguinte formato:

# W dia(s)
# X hora(s)
# Y minuto(s)
# Z segundo(s)

# Obs: Considere que o evento do caso de teste para o problema tem duração 
# mínima de 1 minuto.
# dia 5                               3 dia(s)
# 08 : 12 : 23                        22 hora(s)
# dia 9                               1 minuto(s)
# 06 : 13 : 23                        0 segundo(s)

dia_in_entr = 'dia 5'
hora_in_ent = '07 : 12 : 00'
dia_fim_entr = 'dia 5'
hora_fim_ent = '08 : 12 : 00'
# dia_in_entr = input()
# hora_in_ent = input()
# dia_fim_entr = input()
# hora_fim_ent = input()
dias = 0
horas = 0
minutos = 0
#dias
inicio = int(dia_in_entr[4:])
fim = int(dia_fim_entr[4:])
#começo da festa.
hora_in = int(hora_in_ent[:3])
minuto_in = int(hora_in_ent[5:7])
seg_in = int(hora_in_ent[10:])
# # fim de festa
hora_fim = int(hora_fim_ent[:3])
minuto_fim = int(hora_fim_ent[5:7])
seg_fim = int(hora_fim_ent[10:])

if hora_in < hora_fim and inicio == fim:
    segundos_total = (hora_fim - hora_in) *3600
else:
    segundos_total = (24 - hora_in + hora_fim) * 3600
    segundos_total += (+(minuto_fim - minuto_in)) * 60
    segundos_total += (+(seg_fim - seg_in))

if inicio != fim:
    segundos_total += (fim - inicio -1) * 86400

if segundos_total < 0:
    segundos_total = (+(segundos_total))
if segundos_total >= 86400:
    dias = segundos_total // 86400
    segundos_total -= (dias * 86400)

if segundos_total >= 3600:
    horas = segundos_total // 3600
    segundos_total -= (horas * 3600)

if segundos_total >= 60:
    minutos = segundos_total // 60
    segundos_total -= (minutos * 60)

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos_total} segundo(s)')
