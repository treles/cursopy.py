n = int(input())

for x in range (1,n+1):
    if x % 2 == 0 :
        expotenciaçao = x ** 2
        x = str(x)
        print(x +"^" + "2", "=", expotenciaçao)