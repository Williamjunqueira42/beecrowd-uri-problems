# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
# A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
# As notas consideradas são de 100, 50, 20, 10, 5, 2.
# As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
# A seguir mostre a relação de notas necessárias


d = float(input())
d += 0.001
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, .5, .25, .1, .05, .01]

print('NOTAS:')
for nota in notas:
    qtd = d // nota
    d %= nota
    print(f'{qtd:.0f} nota(s) de R$ {nota:.2f}')



print('MOEDAS:')
for moeda in moedas:
    qtd = d // moeda
    d %= moeda
    print(f'{qtd:.0f} moeda(s) de R$ {moeda:.2f}')
