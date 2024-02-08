
s = 0
d = 1

for n in range(1, 40, 2): 
    s += n/d
    d *= 2

print(f'{s:.2f}')
