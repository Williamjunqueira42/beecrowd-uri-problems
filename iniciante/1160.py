
t=int(input())

for i in range(t):
    ip=input().split(' ')
    pa, pb, g1, g2 = int(ip[0]), int(ip[1]), float(ip[2]), float(ip[3])

    c = 1
    while True:
        pa+=int((g1/100)*pa)
        pb+=int((g2/100)*pb)
        if pa > pb or c > 100:
            if c > 100:
                print('Mais de 1 seculo.')
            else:
                print(c, 'anos.')
            break
        c+=1