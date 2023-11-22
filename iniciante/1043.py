# Triângulo

i = input().split(' ')
A, B, C = float(i[0]), float(i[1]), float(i[2])

if (A + B) > C and (B + C) > A and (C + A ) > B: print(f'Perimetro = {(A+B+C):.1f}')
else:
    s = ((A+B) * C) / 2
    print(f'Area = {s:.1f}')
