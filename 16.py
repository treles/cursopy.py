def menor_numero (numero,numero2):
    numeros = min(numero,numero2)
    return numeros
n1 = int(input('digite um numero'))
n2 = int(input('digite um numero'))
cont = menor_numero(n1,n2)
print(cont)