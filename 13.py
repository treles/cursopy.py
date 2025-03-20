lista = []
for i in range(4):
   num = float(input("Informe um número:"))
   lista.append(num)
   
print(lista)
soma = sum(lista) /4
contador = len(lista)
print(contador)
print(soma)