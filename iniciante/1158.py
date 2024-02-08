
for i in range(int(input())):
    ip = input().split(' ')
    x, y = int(ip[0]), int(ip[1]) 

    if x % 2 == 0: 
        x+=1
    
    n = x + y
    s = 0
    c = 0
    while True:
        s += x
        x += 2
        c += 1
        if c == y: break
    
    print(s)