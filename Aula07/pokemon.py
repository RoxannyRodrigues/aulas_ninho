
class Pokemon:
    def __init__(self, nome, cor, tipo):
        self.nome = nome
        self.cor = cor
        self.tipo = tipo

pokemon1 = Pokemon("Pikachu", "amarelo", "dark")

print(f"""Meu pokemon: nome: {pokemon1.nome} cor: {pokemon1.cor} tipo: {pokemon1.tipo}""")
