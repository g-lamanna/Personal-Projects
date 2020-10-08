import random

class Pokemon():

    def __init__(self, name, level, pok_type, max_health, current_health,knocked_out):
        self.name = name
        self.level = level
        self.pok_type = pok_type
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = knocked_out


    def pokemon_status(self,poke_health):
        self.poke_health = poke_health
        if self.poke_health <= 0:
            return True
        else:
            return False
        

    def lose_health(self,opp_attack_power):
        self.opp_attack_power = opp_attack_power
        if self.current_health == self.max_health:
            self.current_health = self.max_health - self.opp_attack_power
        else:
            self.current_health -= self.opp_attack_power
        if self.current_health < 0:
            self.current_health = 0
        if self.pokemon_status(self.current_health) == True:
            return ("It's super effective! {} taking {} in damage with {} left....{} fainted!".format(poke_Y.name,self.opp_attack_power,self.current_health,poke_Y.name))
        else:
            return("It's super effective! {} taking {} in damage with {} left".format(poke_Y.name,self.opp_attack_power,self.current_health))

    
    def poke_attack(self,poke_X,poke_Y):
        poke_X_attack = 20
        if poke_X.pok_type == "Water" and poke_Y.pok_type == "Fire":
            poke_X_attack += poke_X_attack * 0.40
            self.attack_moves(poke_X,poke_X_attack)
        elif poke_X.pok_type == "Grass" and poke_Y.pok_type == "Water": 
            poke_X_attack += poke_X_attack * 0.40
            self.attack_moves(poke_X,poke_X_attack)
        elif poke_X.pok_type == "Fire" and poke_Y.pok_type == "Grass":
            poke_X_attack += poke_X_attack * 0.40
            self.attack_moves(poke_X,poke_X_attack)
        elif poke_X.pok_type == "Fire" and poke_Y.pok_type == "Water":
            poke_X_attack -= poke_X_attack * 0.40
            self.attack_moves(poke_X,poke_X_attack)
        elif poke_X.pok_type == "Water" and poke_Y.pok_type == "Grass":
            poke_X_attack -= poke_X_attack * 0.40
            self.attack_moves(poke_X,poke_X_attack)
        elif poke_X.pok_type == "Grass" and poke_Y.pok_type == "Fire":
            poke_X_attack -= poke_X_attack * 0.40
            self.attack_moves(poke_X,poke_X_attack)
        
        return self.lose_health(poke_X_attack)

    def attack_moves(self,poke_X,attack_power):
        move = ""
        if poke_X.pok_type == "Grass":
            move = input("Select a move: 'Leaf Blade' or 'Tackle' ")
            if move == "Leaf Blade":
                attack_power += attack_power * 0.25
                print("{} used {}!".format(poke_X.name,move))
                return attack_power
            else:
                print("{} used {}!".format(poke_X.name,move))
                return attack_power
        elif poke_X.pok_type == "Water":
            move = input("Select a move: 'Hydro Pump' or 'Pound' ")
            if move == "Hydro Pump":
                attack_power += attack_power * 0.25
                print("{} used {}!".format(poke_X.name,move))
                return attack_power
            else:
                print("{} used {}!".format(poke_X.name,move))
                return attack_power
        elif poke_X.pok_type == "Fire":
            move = input("Select a move: 'Flame Thrower' or 'Scratch' ")
            if move == "Flame Thrower":
                attack_power += attack_power * 1
                print("{} used {}!".format(poke_X.name,move))
                return attack_power
            else:
                print("{} used {}!".format(poke_X.name,move))
                return attack_power,move



#ATTACKER
poke_X = Pokemon("Squirtle",10,"Water",50,50,False)

#DEFENDER
poke_Y = Pokemon("Charizard",10,"Fire",50,50,False)

poke_Z = Pokemon("Venasaur",10,"Grass",50,50,False)


print(poke_X.poke_attack(poke_Y,poke_X))




