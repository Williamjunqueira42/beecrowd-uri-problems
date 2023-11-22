# Pedrinho está organizando um evento em sua Universidade.
# O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês.
# O problema é que Pedrinho quer calcular o tempo que o evento vai durar,
# uma vez que ele sabe quando inicia e quando termina o evento.
#
# Sabendo que o evento pode durar de poucos segundos a vários dias,
# você deverá ajudar Pedrinho a calcular a duração deste evento.
#
# Entrada
# Como entrada, na primeira linha vai haver a descrição “Dia”,
# seguido de um espaço e o dia do mês no qual o evento vai começar.
# Na linha seguinte, será informado o momento no qual o evento vai iniciar,
# no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato
# das duas primeiras linhas, indicando o término do evento.
#
# Saída
# Na saída, deve ser apresentada a duração do evento, no seguinte formato:
#
# W dia(s)
# X hora(s)
# Y minuto(s)
# Z segundo(s)
#
# Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

dia1 = input().split(' ')
momento1 = (input().replace(' ', '')).split(':')


diaf = input().split(' ')
momentof = (input().replace(' ', '')).split(':')

dias = int(diaf[1]) - int(dia1[1])

sf = int(momentof[0])*3600 + int(momentof[1])*60 + int(momentof[2])
si = int(momento1[0])*3600 + int(momento1[1])*60 + int(momento1[2])

diferençasegundos = sf - si

horas  = diferençasegundos % 3600
diferençasegundos //= 3600

minutos = diferençasegundos % 60
diferençasegundos //= 60

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{diferençasegundos} segundo(s)')
