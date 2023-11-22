X = int(input())

c = 0
n = 0
while True:
    if c == 6:
        break

    if (X + n) % 2 != 0:
        print(X+n)
        c += 1

    n += 1
