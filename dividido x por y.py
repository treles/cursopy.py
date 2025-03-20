N = int(input())
for _ in range(N):
   
    X, Y = map(int, input().split())

    if Y != 0:
        resultado = X / Y
        print("%.1f"%resultado)
    else:
        print("divisao impossivel")