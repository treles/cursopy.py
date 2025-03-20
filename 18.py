def fuc_retorne (x):
    if x % 2 == 0:
        return True
    else:
        return False
    
n1 = int(input('digite um nmero: '))
resultado = fuc_retorne(n1)

if (resultado == False):
    print("O número é impar")
else :
    print("O número é par")
