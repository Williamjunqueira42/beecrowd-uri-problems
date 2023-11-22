# quadrante



while True:

    values = input().split(' ')
    x, y = int(values[0]), int(values[1])

    if x == 0 or y == 0:
        break

    elif x < 0:
        if y > 0: print('segundo')
        if y < 0: print('terceiro')


    elif x > 0:
        if y > 0: print('primerio')
        if y < 0: print('quarto')
