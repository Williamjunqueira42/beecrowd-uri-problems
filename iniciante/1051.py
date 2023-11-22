salario = float(input())


if salario <= 2000:
    print('Isento')


else:
    salario -= 2000 #  parte isenta

    if salario <= 1000:
        imposto = 0.08 * salario
    

    elif salario <= 2500:
         imposto = 0.08 * 1000
         imposto += 0.18 * (salario - 1000)
        


    else:
         imposto = 0.08 * 1000
         imposto += 0.18 * 1500
         imposto += 0.28 * (salario - 2500)


    
    print(f'R$ {imposto:.2f}')
  
    