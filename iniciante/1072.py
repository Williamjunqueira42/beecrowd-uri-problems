# intervalo 2

n = int(input())

valores = []
for x in range(0, n):
    valor = int(input())
    valores.append(valor)

iN = 0
out = 0
for valor in valores:
    if 10 <= valor <= 20: iN += 1
    else: out += 1

print(iN, 'in')
print(out, 'out')
