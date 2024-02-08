
n=int(input())

for i in range(n):
    x=int(input())
    s=0
    for j in range(1, x):
        if x % j == 0 and j != x:
            print(x)
            s+=j
    print(x, end=' ')
    print('eh perfeito' if s == x else 'nao eh perfeito')