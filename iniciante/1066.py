# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares,
# quantos valores digitados foram ímpares, quantos valores digitados foram positivos
#  e quantos valores digitados foram negativos.
#
# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.
#
# Saída
# Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha,
#  não esquecendo o final de linha após cada uma.

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(0, 5):
    n = int(input())
    if n > 0: positivos += 1
    elif n < 0: negativos += 1

    if n % 2 == 0: pares += 1
    else: impares += 1


print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')
