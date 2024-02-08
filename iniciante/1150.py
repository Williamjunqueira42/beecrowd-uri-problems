X=int(input())

while True:
    Z=int(input())
    if Z > X: break

s = X
c = 0

while True:
    if s > Z:
        print(c)
        break 
    c+=1
    s += X+1
