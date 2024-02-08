
n = []
value = float(input())

for i in range(100):
    n.append(value)
    value /= 2

for indice, value in enumerate(n):
    print(f'N[{indice}] = {value:.4f}')