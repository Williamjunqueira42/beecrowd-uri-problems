# Tipo de Combustível

# 1.Álcool 2.Gasolina 3.Diesel 4.Fim

alcool = 0
gasolina = 0
diesel = 0
while True:
    while True:
        i = int(input())
        if i > 0 and i <= 4:
            break

    if i == 1:
        alcool += 1
    elif i == 2:
        gasolina += 1
    elif i == 3:
        diesel += 1
    else:
        break

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
