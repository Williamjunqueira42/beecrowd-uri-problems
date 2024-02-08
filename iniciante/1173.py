v = int(input())
values = []

for i in range(10):
    values.append(v)
    v*=2

for i, v in enumerate(values):
    print(f'N[{i}] = {v}')
