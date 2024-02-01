vinter = 0
vinter = 0
vgremio = 0
empates = 0
while True:
    i = input().split(' ')
    inter = int(i[0])
    gremio = int(i[1])
    if inter > gremio: vinter += 1
    elif gremio > inter: vgremio +=1
    else: empates += 1
    print('Novo grenal (1-sim 2-nao)')
    r = int(input())
    if r == 2:
        break
print(f'{vinter+vgremio+empates} grenais')
print(f'Inter:{vinter}')
print(f'Gremio:{vgremio}')
print(f'Empates:{empates}')
if vinter != vgremio:
    print('Inter venceu mais' if vinter > vgremio else 'Gremio venceu mais')
else:
    print('Nao houve vencedor')
