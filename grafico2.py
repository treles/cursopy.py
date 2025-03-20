import matplotlib.pyplot as plt
meses = ['janeiro','fevereiro','março','abril','maio','junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]
plt.title('faturamento do mes')
plt.xlabel('meses')
plt.xlabel('faturamento em R$')
plt.plot(meses, valores)
plt.show()