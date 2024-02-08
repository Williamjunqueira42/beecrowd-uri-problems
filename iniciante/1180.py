
_ = input()
values = []
input_values = input().split()

for value in input_values:
    values.append(int(value))

min_value = min(values)
pos_min_value = values.index(min_value)
print(f'Menor valor: {min_value}')
print(f'Posicao: {pos_min_value}')
