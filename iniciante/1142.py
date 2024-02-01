# PUM

n = int(input())
value = 0
for l in range(n):
    for n in range(4):
        value += 1
        if n == 3:
            print('PUM')
        else:
            print(value, end=' ')
