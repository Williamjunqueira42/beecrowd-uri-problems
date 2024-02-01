# Na matemática, um Número Primo é aquele que pode ser dividido s
# omente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo,
# pois pode ser dividido apenas pelo número 1 e pelo número 7.
#
# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém
# um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.
#
# Saída
# Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou
 # “X nao eh primo”, de acordo com a especificação fornecida.


N = int(input())
# 0 primo 1 nao primo
for i in range(N):
    r = 0
    value = int(input())
    for n in range(2, value):
        if value % n == 0 and value != n:
            r = 1
    print((f'{value} eh primo') if r == 0 else (f'{value} nao eh primo'))
