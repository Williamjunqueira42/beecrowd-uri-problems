#notas
notas = [100, 50, 20, 10, 5, 2, 1]
v = int(input())
print(v)
for nota in notas:
    n = v // nota
    v %= nota
    qtd = (f'{n} nota(s) de R$ {nota:.2f}').replace('.', ',')
    print(qtd)
