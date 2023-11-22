# Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo,
#  sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora
#  e máxima de 24 horas.
#
# Entrada
# A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
#
# Saída
# Apresente a duração do jogo conforme exemplo abaixo.
i = input().split(' ')
hi, hf = int(i[0]), int(i[1])
dh = hf - hi if hf > hi else (hf+24) - hi
print(f'O JOGO DUROU {dh} HORA(S)')
