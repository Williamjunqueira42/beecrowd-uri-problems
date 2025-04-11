n = int(input())
operation = input()


m = list()

for x in range(12):
    row = list()
    for y in range(12):
        r = float(input())
        row.append(r)

    m.append(row[:])
                 

if operation == 'S':
    print(f'{sum(m[n]):1f}')

if operation == 'M':
    print(f'{(sum(m[n])/12):.1f}')



