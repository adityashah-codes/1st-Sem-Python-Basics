import random

class character:
 
    def __init__(self, name, hp, max_hp, min_dmg, max_dmg, potion, shield, stamina, max_stamina):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.potion = potion
        self.shield = shield
        self.shield_active = False
        self.stamina = stamina
        self.max_stamina = max_stamina

    def dmg(self, crt):
        hit = random.randint(self.min_dmg, self.max_dmg)
        if random.randint(1, 100) <= crt:
            hit = hit * 2
            return hit 
        return hit
    
    def attack(self, target):
        damage = self.dmg(20)
        
        if target.shield_active:
            damage = int(damage * 0.1)
            if damage <= 0:
                damage = 1
            target.shield_active = False
            print(f"Shield absorbed 90% damage ")
        
        
        target.hp = target.hp - damage
        
        if target.hp <= 0:
            target.hp = 0
            print(f"{target.name} fallen")
            return True

        print(f"{self.name} dealt {damage} damage to {target.name}\n{target.name}'s current hp is {target.hp}/{target.max_hp}")
        return False

    def use_potion(self):

        if self.potion > 0:

            if self.hp == self.max_hp:
                print("Your already FUll HEALTH\nCan't use portion")
            else:
                self.hp = self.hp + 25
                self.potion = self.potion - 1
                if self.hp >= self.max_hp:
                    self.hp = self.max_hp
                print(f"{self.name} used one potion\n{self.name}'s current HP:{self.hp}\nPotions's left:{self.potion}") 
            return True
            
        else:
            print(f"You are out of Potions")
            return False        

    def activate_shield(self):
        if self.shield_active:
            print("shield is already active")
            return True
        else:
            if self.shield > 0:
                print("Shield activated")
                self.shield = self.shield - 1
                self.shield_active = True        
                return True
            else:
                print("You are out of shields")
                return False
            
    def check_stamina(self):
        
        if self.stamina <= 20:
            print(f"you are out of stamina\nCurrent stamina:{self.stamina}")
            return True
        else:            
            return False
        
    def recover_stamina(self):
        self.stamina = self.stamina + 25
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina

        print(f"Recovered stamina by 25\ncurrent stamina:{self.stamina}")

    def deduct_stamina(self):
        self.stamina = self.stamina - 20
        if self.stamina < 0:
            self.stamina = 0


class data:
    pass
    
hero = character("Hero", 100, 100, 5, 18, 3, 1, 50, 50)

mon_1 = character("Goblin", 50, 50, 2, 10, 1, 0, 0, 0)
mon_2 = character("Orc Berserker", 50, 50, 2, 10, 1, 0, 0, 0)
mon_3 = character("Mountain Troll", 50, 50, 2, 10, 1, 0, 0, 0)
        
monster_pool = [mon_1, mon_2, mon_3]
enemy = random.choice(monster_pool)

current_turn = "player" 

while hero.hp > 0 and enemy.hp > 0:
  
    if current_turn == "player":

        print(f"\nYour Current enemy:{enemy.name}\n")
     
        action = input("-----------------\n" \
        "Enter 'A' to HIT the Goblin\n" \
        "Enter 'P' to use Portion\n" \
        "Enter 'R' for rest \n" \
        "Enter 'S' to activate shield \n" \
        "Enter 'I' to inspect inventory\n" \
        "Enter 'E to exit\n"
        "----> ")

        if action.upper() == "A":
            
            hero.check_stamina()
            if hero.stamina >= 20:
                
                if hero.attack(enemy):
                    print("You won")                    
                    break
                hero.deduct_stamina()
            else:
                continue
                
            current_turn = "enemy"
        elif action.upper() == "P":
            
            if hero.use_potion():
                
                current_turn = "enemy"
                
        elif action.upper() == "R":
            hero.recover_stamina()
            continue

        elif action.upper() == "S":
            hero.activate_shield()

        elif action.upper() == "I":
            pass

        elif action.upper() == "E":
            pass

    elif current_turn == "enemy":
            
            print(f"{enemy.name} attacks")
            if enemy.attack(hero):
                print("You lost")
                break
            current_turn = "player"
            
                



# print(hero.dmg_to_hero(enemy))
# print(hero.dmg(20))
