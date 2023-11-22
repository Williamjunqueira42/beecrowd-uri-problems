#  Media 3

i = input().split(' ')
N1, N2, N3, N4 = float(i[0]), float(i[1]), float(i[2]), float(i[3])
 # 2, 3, 4 e 1
#media
m = (N1*2 + N2*3 + N3*4 + N4) / 10
print(f'Media: {m:.1f}')

if m >= 7: print('Aluno aprovado.')
elif m < 5: print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    v = float(input())
    print(f'Nota do exame: {v:.1f}')
    m2 = (m + v) / 2
    if m2 >= 5: print('Aluno aprovado.')
    else: print('Aluno reprovado.')
    print(f'Media final: {m2:.1f}')
