# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.


I = input().split(' ')

A = float(I[0])
B = float(I[1])
C = float(I[2])

#Area do Triãngulo retãngulo oque tem A por base e C por altura.
print(f'TRIANGULO: {(A * C / 2):.3f}')

#Area circulo de raio c
pi = 3.14159
print(f'CIRCULO: {pi*C**2:.3f}')

#a área do trapézio que tem A e B por bases e C por altura.
at = ((A + B) * C) / 2
print(f'TRAPEZIO: {at:.3f}')

#a área do quadrado que tem lado B.
print(f'QUADRADO: {(B**2):.3f}')

# a área do retângulo que tem lados A e B.
print(f'RETANGULO: {A*B:.3f}')
