idade1 = int(input("informe a idade"))
idade2 = int(input("informe a idade"))

if idade1 < idade2:
    print("a",idade1,"e mais nova")
elif idade2 < idade1:
    print("a",idade2, "e mais nova")
else:
    print("sao iguais")