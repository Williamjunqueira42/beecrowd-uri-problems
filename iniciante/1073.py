#Quadrado pares
v = int(input())
for i in range(1, v+1):
    if i % 2 == 0:
        print(f'{i}^2 = {i**2}')
