 #requisito 1 - Modelar Pokemon
import random

class Pokemon:
    def __init__(self, nome, tipo, ataque, defesa, velocidade, hp):
        self._nome = nome
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._velocidade = velocidade
        self._hp = hp
        self._movimento = "Ataque rápido"

#Requisito 2 - criar subclasses de pokemon
class Eletrico(Pokemon): 
    def __init__(self, nome,  ataque, defesa, velocidade, hp):
        super().__init__(nome, "Elétrico", ataque, defesa, velocidade, hp)
        self._poder = "Raio de Trovão"

class Aquatico(Pokemon):
    def __init__(self, nome, ataque, defesa, velocidade, hp):
        super().__init__(nome, "Aquático", ataque, defesa, velocidade, hp)
        self._poder = "Jato de Água"

class Fogo(Pokemon):
    def __init__(self, nome, ataque, defesa, velocidade, hp):
        super().__init__(nome, "Fogo", ataque, defesa, velocidade, hp)
        self._poder = "Lança Chama"

class Grama(Pokemon):
    def __init__(self, nome, ataque, defesa, velocidade, hp):
        super().__init__(nome, "Grama", ataque, defesa, velocidade, hp)
        self._poder = "Folhas de Navalhas"

class Ave(Pokemon):
    def __init__(self, nome, ataque, defesa, velocidade, hp):
        super().__init__(nome, "Ave", ataque, defesa, velocidade, hp)
        self._poder = "Folhas de Navalhas"

#classe treinador

class Treinador:
    def __init__(self, nome, pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolherPokemon(self):
        return random.choice(self._pokemons)

class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)
    def escolherPokemon(self):
        while True:
            print(f"Escolha seu pokemon: ")
            for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

            pokemonEscolhido = input("Digite o número do pokemon escolhido: ")
            
            return self._pokemons[int(pokemonEscolhido)-1]
               

"""if (pokemonEscolhido.isnumeric()):
                if (int(pokemonEscolhido) <= len(self._pokemons)):
                    return self._pokemons[int(pokemonEscolhido)-1]
                else:
                    print ("Você escreveu um número maior do que o disponível")
            else:
                print("Você escreveu um caractere inválido")"""


class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)


#função batalha

def batalhaPokemon(treinador1, treinador2):

    p1 = treinador1.escolherPokemon()
    p2 = treinador2.escolherPokemon()

    p1Forca = p1._ataque + p1._defesa + p1._hp
    p2Forca = p2._ataque + p2._defesa + p2._hp

    print(f"{p1._nome} atacou com {p1._movimento} e força {p1Forca}")
    print(f"{p2._nome} atacou com {p2._movimento} e forca {p2Forca}")

    if (p1Forca > p2Forca):
        print(f"O vencedor foi {p1._nome} com força {p1Forca} do treinador {treinador1._nome}")
    elif (p1Forca < p2Forca):
        print(f"O vencedor foi {p2._nome} com força {p2Forca} do treinador {treinador2._nome}")
    else:
        print("Deu empate")

pokemonsDisponiveis = [Fogo("Charmander", 40,30,40,30),
Aquatico("Squirtle", "Aquatico", 30,40,30,30),
Grama("Bulbasaur","Grama", 30,30,30,30),
]


jogador = Jogador("João", [pokemonsDisponiveis[0],pokemonsDisponiveis[1],pokemonsDisponiveis[2]])
inimigo = Inimigo("Bob", [pokemonsDisponiveis])

batalhaPokemon (jogador, inimigo)

