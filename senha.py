def verifica_senha(senha):
    caracteres_especiais = set('!@#$%^&*()-_=+[]{}|;:",.<>?/`~\\')
    numeros = set('0123456789')
    letras = set('abcdefghijklmnopqrstuvwxyz')

    
    count_especiais = 0
    count_numeros = 0
    count_letras = 0
    
    for char in senha:
        if char in caracteres_especiais:
            count_especiais += 1
        elif char in numeros:
            count_numeros += 1
            if char in letras:
                count_letras += 1
    
    return [count_especiais, count_numeros, count_letras]

senha = "a3!@#was"
resultado = verifica_senha(senha)
print(resultado) 
