while True:
    x=int(input())
    if x == 0: break
    c=0
    s=0
    while True:
        if c == 5: break  
        if x % 2 == 0: 
            s+=x
            c+=1 
        x+=1 
    print(s)