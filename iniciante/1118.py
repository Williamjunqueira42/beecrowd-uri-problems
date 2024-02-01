
while True:
    cont = 0
    sum = 0
    while True:
        if cont == 2:
            print(f'media = {sum/2:.2f}')
            break
        n = input()
        if 0 <= float(n) <= 10:
            cont += 1
            sum += float(n)
        else:
            print('nota invalida')

    while True:
        print('novo calculo (1-sim 2-nao)')
        v = input()
        if v == '1' or v == '2':
            break

    if v == '2': break
