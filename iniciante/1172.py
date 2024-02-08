v = []
for i in range(10): 
    value = int(input())
    if value <= 0: value = 1
    v.append(value)

for i, value in enumerate(v):
        print(f'X[{i}] = {value}')






