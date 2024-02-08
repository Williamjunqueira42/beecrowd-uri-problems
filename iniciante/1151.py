#  beecrowd 1051 python
#  WIlliam J

n = int(input())
f = [0, 1]

for i in range(n-2):
    f.append((f[0+i] + f[1+i]))

for number in f:
    if number == f[-1]: print(number)
    else: print(number, end=' ')