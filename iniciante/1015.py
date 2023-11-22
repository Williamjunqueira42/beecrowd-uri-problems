#  Distancia entre dois ponts

p1 = input().split(' ')
p1x, p1y = float(p1[0]), float(p1[1])

p2 = input().split(' ')
p2x, p2y = float(p2[0]), float(p2[1])

d = ((p2x - p1x)**2 + (p2y - p1y)**2)**(0.5)
print(f'{d:.4f}')
