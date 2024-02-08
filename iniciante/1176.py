
for i in range(int(input())):
    n = int(input())
    fibonacci_list = [0, 1]
    for j in range(n):
        fibonacci_list.append((fibonacci_list[0+j] + fibonacci_list[1+j]))
    
    print(f'Fib({n}) = {fibonacci_list[n]}')
    

