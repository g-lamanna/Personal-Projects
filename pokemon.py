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
            return ("{} used water gun! It's super effective! {} taking {} in damage with {} left....{} fainted!".format(poke_X.name,poke_Y.name,self.opp_attack_power,self.current_health,poke_Y.name))
        else:
            return("{} taking {} in damage,still fighting with {} left!".format(poke_Y.name,self.opp_attack_power,self.current_health))

    
    def poke_attack(self,poke_X,poke_Y):
        poke_X_attack = 40
        if poke_X.pok_type == "Water" and poke_Y.pok_type == "Fire":
            poke_X_attack += poke_X_attack * 0.40
        elif poke_X.pok_type == "Grass" and poke_Y.pok_type == "Water": 
            poke_X_attack += poke_X_attack * 0.40
        elif poke_X.pok_type == "Fire" and poke_Y.pok_type == "Grass":
            poke_X_attack += poke_X_attack * 0.40
        elif poke_X.pok_type == "Fire" and poke_Y.pok_type == "Water":
            poke_X_attack -= poke_X_attack * 0.40
        
        return self.lose_health(poke_X_attack)



poke_X = Pokemon("Squirtle",10,"Water",50,50,False)
poke_Y = Pokemon("Charmander",10,"Fire",50,50,False)

print(poke_X.poke_attack(poke_X,poke_Y))




