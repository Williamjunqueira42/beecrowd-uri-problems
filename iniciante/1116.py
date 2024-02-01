i = int(input())
for n in range(i):
    inp = input().split(' ')
    x, y = int(inp[0]), int(inp[1])
    try:
        print(round(x/y, 1))
    except:
        print('divisao impossivel')
