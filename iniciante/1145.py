ip = input().split(' ')
x, y = int(ip[0]), int(ip[1])

values = list(range(1, y+1))

c = 0
for value in values:
    c += 1
    if c == x:
        print(value)
        c = 0
    else:
        print(value, end=' ')
    
    
