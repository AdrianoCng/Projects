from Trainer import Trainer;

class Pokemon:

    def __init__(self, name, level, element, max_health, current_health):
        self.name = name;
        self.level = level;
        self.type = element;
        self.max_health = max_health;
        self.health = current_health;
        self.is_knocked_out = False;

    def __repr__(self):
        return self.name;



    # The pokemon take damage and is knocked out if its health is <= 0
    def lose_health(self, dmg):
        self.health -= dmg;
        print(self.name + " loses " + str(dmg) + " health and has now " + str(self.health));
        if (self.health <= 0):
            self.knock_out();




    # return False if the pokemon is already max hps, True if reg health
    def gain_health(self, health):
        if (self.health >= self.max_health):
            print(self.name + " is already full hps");
            return False;
        else:
            self.health += health;

            # Cap Pokemon's health to its max_health stat
            if (self.health > self.max_health):
                self.health = self.max_health;

        print(self.name + " regenerates " + str(health) + " health and has now " + str(self.health) + " health");
        return True;



    def knock_out(self):
        print(self.name + " is KO");
        self.is_knocked_out = True;



    def revive(self):
        if self.is_knocked_out:
            print(self.name + " is revived");
            self.health = self.max_health;
            self.is_knocked_out = False;
        else:
            print(self.name + " is not KO");


    # This function takes another pokemon as argument and attacks him.
    # The damage is calculated based on the (attacker)pokemon type and level
    # the damage is then passed as argument to lose_health() on the enemy pokemon instance
    def attack(self, enemy_pokemon):
        if (self.is_knocked_out == True):
            print(self.name + " is KO. Cannot attack");
            return False;

        print(self.name + " attacks " + enemy_pokemon.name);
        print(self.name + " is of type " + self.type + " and " + enemy_pokemon.name + " is of type " + enemy_pokemon.type);
        
        dmg = self.level;

        # if attacker type is fire
        if (self.type == "fire"):
            if (enemy_pokemon.type == "water"):
                print(self.name + " attack is not very effective");
                dmg /= 2;
            elif (enemy_pokemon.type == "grass"):
                print(self.name + " attack is very effective!");
                dmg *= 2;

        # if attacker type is water
        elif (self.type == "water"):
            if (enemy_pokemon.type == "fire"):
                print(self.name + " attack is very effective!");
                dmg *= 2;
            elif (enemy_pokemon.type == "grass"):
                print(self.name + " attack is not very effective");
                dmg /= 2;

        # if attacker type is grass
        elif (self.type == "grass"):
            if (enemy_pokemon.type == "fire"):
                print(self.name + " attack is not very effective");
                dmg /= 2;
            elif (enemy_pokemon.type == "water"):
                print(self.name + " attack is very effective!");
                dmg *= 2;

        print(self.name + " hits for " + str(dmg) + " dmg");

        enemy_pokemon.lose_health(dmg);




# Pokemons
pikachu = Pokemon("pikachu", 50, "fire", 100, 100);
charisard = Pokemon("charisard", 50, "water", 100, 100);
golum = Pokemon("golum", 50, "grass", 100, 100);
squirle = Pokemon("squirle", 50, "fire", 100, 100);
tartlu = Pokemon("tartlu", 50, "water", 100, 90);
dino = Pokemon("dino", 50, "grass", 100, 100);


# Trainers
alex = Trainer("Alex", 1, [pikachu, charisard, golum]);
gigi = Trainer("Gigi", 5, [squirle, tartlu, dino]);


# call methods
alex.attack(gigi);
alex.use_potions();
print("\n");
gigi.switch_pokemon(1);
gigi.attack(alex);
print("\n");
alex.revive(0);
alex.switch_pokemon(2);
alex.attack(gigi);
print("\n");
gigi.attack(alex);
gigi.switch_pokemon(2);
gigi.attack(alex);
print("\n");
alex.use_potions();
alex.use_potions();
alex.view_pokemons_stats();
print("\n");
print(alex);