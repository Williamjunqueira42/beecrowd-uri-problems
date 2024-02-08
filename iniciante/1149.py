# Faça um algoritmo para ler um valor A e um valor N.
# Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1).
# Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

# Entrada
# A entrada contém somente valores inteiros,
# podendo ser positivos ou negativos. Todos os valores estão na mesma linha.

# Saída
# A saída contém apenas um valor inteir


ip = input().split(' ')
A = int(ip[0])

c = 1
while True:
    N = int(ip[c])
    if N > 0: break
    c+=1

s = 0
for i in range(0, N):
    s += A + i

print(s)
