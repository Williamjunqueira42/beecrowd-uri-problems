#resto da divisãop
x = int(input())
y = int(input())
mn = min(x, y)
mx = max(x, y)
for i in range(mn, mx):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
