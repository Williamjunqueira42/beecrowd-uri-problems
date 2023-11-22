i = input().split(' ')
x, y = float(i[0]), float(i[1])

if x == 0 or y == 0:
    if x != 0: print('Eixo X')
    elif y != 0: print('Eixo Y')
    else:  print('Origem')

elif x > 0:
    if y > 0: print('Q1')
    else: print('Q4')

else:
    if y > 0: print('Q2')
    else: print('Q3')
