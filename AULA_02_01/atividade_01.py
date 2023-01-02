import random

especiesPokemon = ("Pidgeot","Farfetch'd", "Pikachu","Bulbasaur", "Charizard", "Squirtle")

meuPokemon  = random.choice(especiesPokemon)

match meuPokemon:
    case "Pidgeot":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)

    case "Farfetch'd":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)
    
    case "Pikachu":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)
    
    case "Bulbasaur":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)

    case "Charizard":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)
    
    case "Squirtle":
        meuPokemonAtaque = random.randint(30,50)
        meuPokemonDefesa = random.randint(30,50)
        meuPokemonHp = random.randint(30,50)

pokemoninimigo = random.choice(especiesPokemon)

match pokemoninimigo:
    case "Pidgeot":
        pokemoninimigoAtaque = random.randint(30,50)
        pokemoninimigoDefesa = random.randint(30,50)
        pokemoninimigoHp = random.randint(30,50)

    case "Farfetch'd":
       pokemoninimigoAtaque = random.randint(30,50)
       pokemoninimigoDefesa = random.randint(30,50)
       pokemoninimigoHp = random.randint(30,50)
    
    case "Pikachu":
       pokemoninimigoAtaque = random.randint(30,50)
       pokemoninimigoDefesa = random.randint(30,50)
       pokemoninimigoHp = random.randint(30,50)
    
    case "Bulbasaur":
       pokemoninimigoAtaque = random.randint(30,50)
       pokemoninimigoDefesa = random.randint(30,50)
       pokemoninimigoHp = random.randint(30,50)

    case "Charizard":
       pokemoninimigoAtaque = random.randint(30,50)
       pokemoninimigoDefesa = random.randint(30,50)
       pokemoninimigoHp = random.randint(30,50)
    
    case "Squirtle":
       pokemoninimigoAtaque = random.randint(30,50)
       pokemoninimigoDefesa = random.randint(30,50)
       pokemoninimigoHp = random.randint(30,50)


forçameuPokemon = + meuPokemonAtaque + meuPokemonDefesa + meuPokemonHp
forçapokemoninimigo =  pokemoninimigoAtaque + pokemoninimigoDefesa + pokemoninimigoHp

if forçameuPokemon > forçapokemoninimigo:
    print (f'Meu pokemon: {meuPokemon} Ganhou')
elif forçameuPokemon < forçapokemoninimigo:
     print (f'Pokemon inimigo: {pokemoninimigo} Ganhou')
else:
    print (f'Meu Pokemon e Pokemon inimigo Empataram')

