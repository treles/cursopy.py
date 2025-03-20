def quiz():
    perguntas = [
        {
            "pergunta": "Qual é a capital do Japão?",
            "opcoes": ["A) Pequim", "B) Seul", "C) Tóquio", "D) Berlim"],
            "resposta": "C"
        },
        {
            "pergunta": "Qual é o maior oceano do mundo?",
            "opcoes": ["A) Atlântico", "B) Índico", "C) Ártico", "D) Saturno"],
            "resposta": "C"
        },
        {
            "pergunta": "Quem escreveu Hamlet?",
            "opcoes": ["A) Charles Dickens", "B) William Shakespeare", "C) Dante Alighieri", "D) J.K. Rowling"],
            "resposta": "A"
        }
    ]

    pontuacao = 0

    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for opcao in pergunta["opcoes"]:
            print(opcao)
        
        resposta_usuario = input("Digite a letra da sua resposta: ").upper()

        if resposta_usuario == pergunta["resposta"]:
            print("Correto!\n")
            pontuacao += 1
        else:
            print("Errado. A resposta correta é", pergunta["resposta"], "\n")

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")

quiz()