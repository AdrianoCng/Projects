class Trainer:
    def __init__(self, name, potions, pokemons):
        self.name = name;
        self.potions = potions;
        self.pokemons = pokemons;
        self.current_pokemon = self.pokemons[0];

    def __repr__(self):
        return """
            name: {name};
            potions: {potions};
            pokemons: {pokemons};
            current pokemon: {current_pokemon};
            """.format(name=self.name, potions=self.potions, pokemons=self.pokemons, current_pokemon=self.current_pokemon);


    # Heal for 20 hps
    def use_potions(self):
        if (self.potions > 0):
            print(self.name + " use a potion");

            # "healed" Is False if the pokemon was already full hps || True if the pokemon has been healed
            healed = self.current_pokemon.gain_health(20);
            if (healed):
                self.potions -= 1;
                print(self.name + " has now " + str(self.potions) + " potions left");
            else:
                print(self.name + " still has " + str(self.potions) + " potions left");

        else:
            print(self.name + " tries to use a potion but doesn't have enough");



    def attack(self, enemy_trainer):
        print(self.name + " attacks " + enemy_trainer.name + " with " + self.current_pokemon.name);
        self.current_pokemon.attack(enemy_trainer.current_pokemon);



    def switch_pokemon(self, pokemon):
        pokemon_to_call = self.pokemons[pokemon];
        if (pokemon_to_call.is_knocked_out):
            print(pokemon_to_call.name + " is KO");
            print("Call another pokemon!");
        elif (pokemon_to_call == self.current_pokemon):
            print(pokemon_to_call.name + " is already fighting!");
        else:
            self.current_pokemon = pokemon_to_call;
            print(self.name + " calls " + pokemon_to_call.name + "!");



    def revive(self, pokemon):
        pokemon_to_revive = self.pokemons[pokemon];
        print(self.name + " try to revive " + pokemon_to_revive.name);

        if (pokemon_to_revive.is_knocked_out):
            pokemon_to_revive.revive();
            print(pokemon_to_revive.name + " is now full hps and ready to fight!!!");
        else:
            print(pokemon_to_revive.name + " is still alive");



    def view_pokemons_stats(self):
        for pokemon in self.pokemons:
            print("""
                name: {name};
                level: {level};
                type: {type}:
                max health: {max_health};
                health: {health};
                is ko: {is_ko};
                """.format( name=pokemon.name, 
                            level=pokemon.level,
                            type=pokemon.type, 
                            max_health=pokemon.max_health, 
                            health=pokemon.health, 
                            is_ko=pokemon.is_knocked_out));