I = input().split(' ')
a, b, c = int(I[0]), int(I[1]), int(I[2])

MaiorAB = (a + b + abs(a-b)) / 2
MaiorABC = (MaiorAB + c + abs(MaiorAB - c)) / 2

print(f'{int(MaiorABC)} eh o maior')
