nome = input()
quantidades_de_vendas = float(input())
salario_fixo = float(input())

bonus = (salario_fixo * 0.15) + quantidades_de_vendas
print('TOTAL = R$%.2f'%bonus)