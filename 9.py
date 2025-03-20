nome1 = str(input("fale o seu nome: "))
idade1 = int(input("informe a idade"))
nome2 = str(input("fale o seu nome: "))
idade2 = int(input("informe a idade"))

if idade1 > idade2:
    print("a",nome1,"e mais velho")
elif idade2 > idade1:
    print("a",nome2, "e mais velho")
else:
    print("tem a mesma idade")