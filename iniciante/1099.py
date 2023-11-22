

n = int(input())
somas = []

for i in range(n):
    values = input().split(' ')

    X, Y = int(values[0]), int(values[1])
    maior = max(X, Y)
    menor = min(X, Y)

    s = 0
    for j in range(menor+1, maior):
        if j % 2 != 0:
            s += j
    somas.append(s)
        
for soma in somas:
    print(soma)