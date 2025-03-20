def contar_valores(lista):
    pares = impares = positivos = negativos = 0
    for valor in lista:
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1
    
    return pares, impares, positivos, negativos

# Entrada dos valores
valores = []
for i in range(5):
    valor = int(input())
    valores.append(valor)

# Contar valores pares, ímpares, positivos e negativos
pares, impares, positivos, negativos = contar_valores(valores)

# Saída
print((pares),"valor(es) par(es)")
print((impares),"valor(es) impar(es)")
print((positivos),"valor(es) positivo(s)")
print((negativos),"valor(es) negativo(s)")