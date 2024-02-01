i = 1
j = 7

while True:
    for n in range(3):
        print(f'I={i}', f'J={j}')
        j -= 1
    if i == 9: break
    j = 7
    i += 2
