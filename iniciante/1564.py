

while True: 
    try:
        r = int(input())
        print('vai ter copa!' if r == 0 else 'vai ter duas!')

    except EOFError:
        break


