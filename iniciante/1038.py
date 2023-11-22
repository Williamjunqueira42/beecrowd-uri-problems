
preços = [4, 4.50, 5, 2, 1.50]

i = input().split(' ')
a, b = int(i[0]), int(i[1])

t = preços[a-1] * b
print(f'Total: R$ {t:.2f}')
