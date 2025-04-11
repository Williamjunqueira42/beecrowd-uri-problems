

matriz = list()
C = int(input()) # column number 
T = input()
# for x in range(12):
#     row = []
#     for y in range(12):
#         value = float(input())
#         row.append(value)
#     matriz.append(row[:])


matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


column = list()
for row in matriz2:
    element = row[C]
    column.append(element)


if T == 'S':
    print(f'{sum(column):.1f}')

elif T == 'M':
    lenght = len(column)
    print(f'{(sum(column)/lenght):.1f}')
