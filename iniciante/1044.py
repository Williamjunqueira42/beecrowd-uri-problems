

i = input().split(' ')
a, b = int(i[0]), int(i[1])
print('Sao Multiplos' if b%a == 0 or a%b == 0 else 'Nao sao Multiplos')
