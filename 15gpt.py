notas = []
total_notas = 0
soma_notas = 0

# Entrada de notas
while True:
    nota = float(input("Digite uma nota (ou um número negativo para sair): "))
    if nota < 0:
        break
    notas.append(nota)
    total_notas += 1
    soma_notas += nota

# Mostrar a quantidade de notas lidas
print(f"\nQuantidade de notas lidas: {total_notas}")

# Exibir todas as notas na ordem em que foram informadas
print("\nNotas na ordem em que foram informadas:")
for nota in notas:
    print(nota)

# Exibir todas as notas na ordem inversa à que foram informadas
print("\nNotas na ordem inversa à que foram informadas:")
for nota in reversed(notas):
    print(nota)

# Calcular e mostrar a soma das notas
print(f"\nSoma das notas: {soma_notas}")

# Calcular e mostrar a média das notas
media_notas = soma_notas / total_notas
print(f"Média das notas: {media_notas:.2f}")

# Calcular e mostrar a quantidade de notas acima da média
notas_acima_media = sum(nota > media_notas for nota in notas)
print(f"Quantidade de notas acima da média:"),(notas_acima_media)