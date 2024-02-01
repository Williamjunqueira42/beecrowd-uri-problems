i = 1
j = 7
s = 0
while True:
    for n in range(3):
        print(f'I={i}', f'J={j}')
        j -= 1
    if i == 9: break
    s += 2
    j = 7 + s
    i += 2
