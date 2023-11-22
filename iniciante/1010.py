peça1 = input().split(' ')
peça2 = input().split(' ')

valor_peça1 = int(peça1[1]) * float(peça1[2])
valor_peça2 = int(peça2[1]) * float(peça2[2])
valor_total = valor_peça1 + valor_peça2

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')
