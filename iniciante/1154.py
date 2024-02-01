sum, cont = 0, 0
while True:
    v = int(input())
    if v < 0: break
    sum += v
    cont += 1
print(f'{sum/cont:.2f}')
