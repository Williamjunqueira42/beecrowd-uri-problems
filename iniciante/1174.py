
a = []
for i in range(100):
    a.append(float(input()))

for i, x in enumerate(a):
    if x <= 10:
        print(f'A[{i}] = {x:.1f}')