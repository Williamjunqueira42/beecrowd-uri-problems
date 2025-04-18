# Entrada
# A primeira linha de entrada contém um número inteiro QT (1 ≤ QT ≤ 100), indicando a quantidade de casos de teste que vem a seguir. Cada caso de teste contém duas linhas. Na primeira linha será informado o nome do jogador 1 seguido de sua escolha, “PAR” ou “IMPAR” e logo após, o nome do jogador 2 seguido de sua escolha, “PAR” ou “IMPAR”. Na segunda linha de entrada, contém 2 números inteiros N (1 ≤ N ≤ 10⁹) e M (1 ≤ M ≤ 10⁹), representando respectivamente os números escolhidos pelo jogador 1 e pelo jogador 2. É garantido que a escolha (PAR ou IMPAR) do jogador 1 será diferente da escolha (PAR ou IMPAR) do jogador 2 e que o nome dos jogares são formados somente por letras e não ultrapassarão 100 caracteres.

# Saída
# Para cada caso de teste, imprima uma única linha contendo o nome do jogador vencedor.


QT =int(input())

for x in range(QT):
    information = input().split()
    numbers = input().split()
    s = 0
    for n in numbers: s += int(n) 
    isodd = (s % 2 != 0)
    print(information[information.index('IMPAR' if isodd else 'PAR') - 1])
  