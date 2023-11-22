#experiencia


n = int(input())

cobaias, coelhos, ratos, sapos = 0, 0, 0, 0
for i in range(n):

    inp = input().split(' ')
    qtd = int(inp[0])
    especie = inp[1]

    cobaias += qtd
    if especie == 'C':
        coelhos += qtd
    elif especie == 'R':
        ratos += qtd
    else:
        sapos += qtd

print(f'Total: {cobaias} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos:{(coelhos/cobaias)*100:.2f} %')
print(f'Percentual de ratos:{(ratos/cobaias)*100:.2f} %')
print(f'Percentual de sapos:{(sapos/cobaias)*100:.2f} %')
