def  calcular_pagamento (qtd_horas,valo_hora):
    horas = float(qtd_horas)
    taxa = float(valo_hora)
    if horas <=40:
        salario = horas*taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))
    return salario
horas=input('digite as horas: ')
taxa=input('digite a taxa: ')
total_salario = calcular_pagamento(horas,taxa)
print('o valor de seus redimentos é R$: ',total_salario)