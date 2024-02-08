
def print_vector(vector, type):
    for index, value in enumerate(vector):
        print(f'{type}[{index}] = {value}')


odd_vector = []
even_vector = []

for x in range(15):
    number = int(input())
    if number % 2 == 0:
        even_vector.append(number)

    else:
        odd_vector.append(number)

    if len(even_vector) == 5:
        print_vector(even_vector, 'par')
        even_vector = []

    elif len(odd_vector) == 5:
        print_vector(odd_vector, 'impar')
        odd_vector = []


print_vector(odd_vector, 'impar')
print_vector(even_vector, 'par')

