#anos em dias
i  = int(input())
anos = i // 365
i %= 365

meses = i // 30
i %= 30
dias = i

print(anos, 'ano(s)')
print(meses, 'mes(es)')
print(dias, 'dia(s)')
