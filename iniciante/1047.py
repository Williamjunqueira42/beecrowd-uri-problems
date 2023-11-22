# Tempo de Jogo com Minutos

i = input().split(' ')

hora_inicial = int(i[0])
minuto_inicial = int(i[1])
hora_final = int(i[2])
minuto_final = int(i[3])


diferença_hora = (hora_final - hora_inicial) if hora_final > hora_inicial else (24 - (hora_inicial - hora_final))
diferença_minuto = minuto_final - minuto_inicial if minuto_final >= minuto_inicial else (60 - (minuto_inicial - minuto_final))

if diferença_hora == 24 and diferença_minuto != 0:
    if diferença_minuto != 59: h = 0
    elif diferença_minuto == 59: h = 23


else:
    h = diferença_hora + (diferença_minuto // 60)

m = diferença_minuto % 60

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')
