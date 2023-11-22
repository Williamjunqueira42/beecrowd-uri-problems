#sort simples
i = input().split(' ')
valores = []
for v in i: valores.append(int(v))

valores_em_ordem = valores[:]
valores_em_ordem.sort()
for valor in valores_em_ordem: print(valor)

print()

for valor in valores: print(valor)
