# Entrada
# Um número inteiro C será informado, 
# que será a quantidade de casos de teste. Cada caso de teste inicia com um número
# inteiro N (1 ≤ N ≤ 1000), indicando a quantidade de termos da soma.

# Saída
# Para cada caso de teste imprima um número S, 
# que é o resultado da soma dos N termos da expressão


C = int(input())
for x in range(C):
    n = int(input())
    is_odd = (n % 2 != 0)
    print(1 if is_odd else 0)
    


