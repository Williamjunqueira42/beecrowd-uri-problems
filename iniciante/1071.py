X = int(input())
Y = int(input())
values = list(range(X+1, Y)) if X <= Y else list(range(Y+1, X))

sum = 0

for value in values:
    if value % 2 != 0: sum += value

print(sum)
