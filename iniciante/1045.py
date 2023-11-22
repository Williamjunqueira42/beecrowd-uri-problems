i = input(). split(' ')

lados = []
for x in i:
    lados.append(float(x))

lados.sort(reverse=True)
A, B, C = lados[0], lados[1], lados[2]

if A >= B + C: print('NAO FORMA TRIANGULO')
elif A**2 == B**2 + C**2: print('TRIANGULO RETANGULO')
elif A**2 > B**2 + C**2: print('TRIANGULO OBTUSANGULO')
else: print('TRIANGULO ACUTANGULO')

if A == B == C: print('TRIANGULO EQUILATERO' )
elif A == B or B == C or C == A: print('TRIANGULO ISOSCELES')
