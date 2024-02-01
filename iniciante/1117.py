c = 0
s = 0
while True:
    n = input()
    if 0 < float(n) <= 10:
        c += 1
        s += float(n)
    else: print('nota invalida')
    if c == 2:
        break

print('media =', round(s/2, 2))
