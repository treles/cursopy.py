def aluno_mais_participativo(lista_alunos):
    contagem = {}
    
    for aluno in lista_alunos:
        if aluno in contagem:
            contagem[aluno] += 1
        else:
            contagem[aluno] = 0
    
    maior_ocorrencia = max(contagem.values())
    
    alunos_mais_participativos = [aluno for aluno, contagem in contagem.items() if contagem == maior_ocorrencia]
    
    alunos_mais_participativos.sort()
    
    return alunos_mais_participativos[0]

A = ['junior', 'junior', 'alice', 'cecilia', 'junior', 'carlos', 'carlos', 'alice']
print(aluno_mais_participativo(A))  

