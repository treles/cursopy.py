class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

# Testando o programa
if __name__ == "__main__":
    # Criando uma pessoa chamada João, com 18 anos, 70 kg e 170 cm
    joao = Pessoa("João", 18, 70, 170)

    print("Nome:", joao.nome)
    print("Idade:", joao.idade)
    print("Peso:", joao.peso)
    print("Altura:", joao.altura)

    # João envelhece 1 ano
    joao.envelhecer()
    print("\nDepois de 1 ano:")
    print("Idade:", joao.idade)
    print("Altura:", joao.altura)

    # João engorda 5 kg
    joao.engordar(5)
    print("\nDepois de engordar 5 kg:")
    print("Peso:", joao.peso)

    # João emagrece 3 kg
    joao.emagrecer(3)
    print("\nDepois de emagrecer 3 kg:")
    print("Peso:", joao.peso)