while True:
    inp = input().split()
    x, y = int(inp[0]), int(inp[1])
    if x == y:
        break
    elif x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
