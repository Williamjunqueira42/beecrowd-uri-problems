
# Sequencia de Numeros e Soma
while True:
    i = input().split()
    m, n = int(i[0]), int(i[1])
    if m <= 0 or n <= 0: break
    mi = min(m, n)
    mx = max(m, n)
    sum = 0
    for value in range(mi, mx+1):
        print(value, end=' ')
        sum += value

    print(F'Sum={sum}')
