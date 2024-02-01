i = 0
j = 1
while True:
    if i > 2:
        break

    for n in range(3):
        if i // 1 == i:
            I = int(i)
            J = int(j+i)
        else:
            I = round(i, 1)
            J = round(j+i, 1)

            if I == 2:
                I = 2
                J = int(j+i)


        print(f'I={I} J={J}')
        j += 1
    j = 1
    i += .2
