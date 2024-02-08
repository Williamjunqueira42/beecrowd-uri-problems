

t=int(input())
v=[*range(0, t)]
values = []
c = 0

while True:
    if len(values) >= 1000: break
    values.append(v[c])
    if c >= t-1: c=0    
    else: c+=1

for i, value in enumerate(values):
    print(f'N[{i}] = {value}')

