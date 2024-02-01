# Múltiplos de 13

x = int(input())
y = int(input())

mn = min(x, y)
mx = max(x, y)
sum = 0
for value in range(mn, mx+1):
    if value % 13 != 0:
        sum += value
print(sum)
