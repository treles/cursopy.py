def quiz():
    perguntas = [
        {"pergunta":"Qual o seu nome?",
         'opcoes': ['A Carlos', 'B Marcus', 'C Adriel'],
         'resposta':'A'
         },
        {"pergunta":"Qual o meu nome?",
         'opcoes': ['A Carlos', 'B Marcus', 'C Adriel'],
         'resposta':'C'},
        {"pergunta":"Qual o seu nome?",
         "opcoes": ["A Carlos", "B Marcus", "C Adriel"],
         "resposta":"A"
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