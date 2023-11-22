#  Gasto Combustivel

# Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L.
# Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas)
# e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida,
# calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.


#12 km / l

t = int(input())
vm = int(input())
d = t * vm
qtd = d / 12
print(f'{qtd:.3f}')
