

s = float(input())
p = 0

if s <= 400: p = .15
elif s <= 800: p = .12
elif s <= 1200: p = .1
elif s <= 2000: p = .07
else: p = .04

a = p*s
s += a

print(f'Novo salario: {s:.2f}')
print(f'Reajuste ganho: {a:.2f}')
print(f'Em percentual: {int(p*100)} %')
