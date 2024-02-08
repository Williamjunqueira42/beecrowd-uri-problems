
n = list()
for i in range(20):
    n.append(int(input()))

n_invert = n[::-1]  

for i, v in enumerate(n_invert):
    print(f'N[{i}] = {v}')
