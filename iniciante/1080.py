values = []

for n in range(100):
    value = int(input())
    values.append(value)

max_value = max(values, key=int)
pos = values.index(max_value)

print(max_value)
print(pos+1)