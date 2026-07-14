import random
import json

#----variables----

hero_hp = 100
stamina = 50
inv = ["potion", "potion", "potion", "shield"]
total_wins = 0
total_dungeon_wins = 0

#----Monsters-----

monster_pool = [
    {
        "name": "Goblin",
        "hp": 50,
        "max_hp": 50,
        "min_dmg": 2,
        "max_dmg": 10,
    },
    {
        "name": "Orc Berserker", 
        "hp": 100, 
        "max_hp": 100, 
        "min_dmg": 8, 
        "max_dmg": 18,
    },
    {
        "name": "Mountain Troll",
        "hp": 160, 
        "max_hp": 160, 
        "min_dmg": 12,
        "max_dmg": 26,
    }
]

#----Battle History

try:
    with open ("save_data.json", "r") as file:
        save_state = json.load(file) # uses old stats to continue progress
        
        total_wins = save_state.get("total_wins", 0)
        inv = save_state.get("inv", ["potion", "potion", "potion", "shield"])
        total_dungeon_wins = save_state.get("total_dungeon_wins", 0)
        
        print(f"Welcome back\nTotal Single battle won: {total_wins}\nTotal Dungeon battle won:{total_dungeon_wins}")

except FileNotFoundError:
    total_wins = 0
    total_dungeon_wins = 0
    inv = ["potion", "potion", "potion", "shield"]

#----functions----

def dmg(min, max, crt): # damage dealer
    hit = random.randint(min, max)
    if random.randint(1, 100) == crt:
        hit = hit*2
        return hit, True
    return hit, False

def use_item(item): # inv item user
    global hero_hp, inv
    if item in inv:
 
        if item == "potion":
            heal_amt = 25
            hero_hp = hero_hp + heal_amt
            if hero_hp >=100:
                hero_hp = 100
            inv.remove("potion")
            print(f"You used one Portion\n Current HP : {hero_hp}")
            return True
 
        elif item == "shield":
            print("----Shield activated----")
            inv.remove("shield")
            return True

    else:
        print(f"You are out of {item}")
        return False        

#----Main loop----

while True:
    
    primary_action = input("-----------------\nChoose Your Game Mode\nEnter '1' to battle a random Monster\nEnter '2' for Dungeon Battle\nEnter 'E'to exit\n-----------------\n-----> ")
    
    if primary_action == "1": # single monster mode
        
        current_enemy = random.choice(monster_pool).copy() # Chooses Random Monster
        print(f"You encountered {current_enemy}!!\n Choose Your action")

        shield_is_active = False

        while hero_hp > 0 and current_enemy["hp"] > 0:
            
            print("----BATTLE BEGINS----")

            if shield_is_active == True:
                print("Shield activated")
                
            else:                
                print("Choose your action")

            action = input("-----------------\nEnter 'A' to HIT the Goblin\nEnter 'P' to use Portion\nEnter 'R' for rest \nEnter 'S' to activate shield \nEnter 'I' to inspect inventory\nEnter 'E to exit\n----> ")

            if action.upper() == "A": # hero's attack
                
                if stamina > 10: # hero can attack
                    stamina = stamina - 15
                    dmg_to_monster, is_crt = dmg(10, 18, 20)
                    current_enemy["hp"] = current_enemy["hp"] - dmg_to_monster
                
                    if current_enemy["hp"] <= 0:
                        print(f"You defeated {current_enemy['name']}")
                        total_wins = total_wins + 1 # Stats 
                        print(f"Your total Victory {total_wins}")
                        current_save = {
                                        "total_wins": total_wins,
                                        "total_dungeon_wins": total_dungeon_wins,  
                                        "inv": inv
                                        }
                        with open("save_data.json", "w") as file: # saving stats
                            json.dump(current_save, file, indent=4)
                        print("Progress saved")        
                        break
                    
                    if is_crt: # critical attack
                        print(f"BOOM!!, CRITICAL DEAlT 2x DAMAGE!!\n Damage Dealt {dmg_to_monster}\n {current_enemy['name']} Current HP : {current_enemy['hp']}")
                    else: # normal attack
                        print(f"You hitted goblin and dealt damge {dmg_to_monster}\n {current_enemy['name']} Current HP : {current_enemy['hp']}")
                
                else: # hero can't attack
                    print("You are out of stamina\nRest for a while (use 'R') : ")
                    continue

                # Monster's attack
                dmg_to_hero , is_crt = dmg(current_enemy["min_dmg"], current_enemy["max_dmg"], 10)
                if shield_is_active:
                    dmg_to_hero = dmg_to_hero - 10
                    if dmg_to_hero <= 0:
                        dmg_to_hero = 0
                    shield_is_active =False
            
                hero_hp = hero_hp - dmg_to_hero
                
                if hero_hp <= 0: #Monster won
                    print(f"{current_enemy['name']} won , Try again ;)")
                
                else:
                    if is_crt: # Monster's critical attack
                        print(f"OOuch, {current_enemy['name']} Hitted You with a critical \n It dealt a damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")
                    else: # Monster's normal attack
                        print(f"{current_enemy['name']} Hitted you and dealt damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")

            elif action.upper() == "P": # healing
                item_used = use_item("potion")
                
                if not item_used:
                    continue

                # Monster's attack
                dmg_to_hero , is_crt = dmg(current_enemy["min_dmg"], current_enemy["max_dmg"], 10)
                if shield_is_active:
                    dmg_to_hero = dmg_to_hero - 10
                    if dmg_to_hero <= 0:
                        dmg_to_hero = 0
                    shield_is_active =False
                hero_hp = hero_hp - dmg_to_hero
                
                if hero_hp <= 0: #Monster won
                    print(f"{current_enemy['name']} won , Try again ;)")
                
                else:
                    if is_crt: # Monster's critical attack
                        print(f"OOuch, {current_enemy['name']} Hitted You with a critical \n It dealt a damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")
                    else: # Monster's normal attack
                        print(f"{current_enemy['name']} Hitted you and dealt damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")

            elif action.upper() == "R": # stamina recovery
                stamina = stamina + 25
                
                if stamina >= 50:
                    stamina = 50
                print(f"You took a nap\n Your current stamina {stamina}")

                # Monster's attack
                dmg_to_hero , is_crt = dmg(current_enemy["min_dmg"], current_enemy["max_dmg"], 10)
                if shield_is_active:
                    dmg_to_hero = dmg_to_hero - 10
                    if dmg_to_hero <= 0:
                        dmg_to_hero = 0
                    shield_is_active =False
                hero_hp = hero_hp - dmg_to_hero
                
                if hero_hp <= 0: #Monster won
                    print(f"{current_enemy['name']} won , Try again ;)")
                
                else:
                    if is_crt: # Monster's critical attack
                        print(f"OOuch, {current_enemy['name']} Hitted You with a critical \n It dealt a damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")
                    else: # Monster's normal attack
                        print(f"{current_enemy['name']} Hitted you and dealt damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")

            elif action.upper() == "S": # shield activation with re-action chance

                if use_item("shield"):
                    shield_is_active = True
                    continue
                else:
                    continue
                                
            elif action.upper() == "I": # Display"s inventory items
                
                total_potion = inv.count("potion")
                total_shield = inv.count("shield")
                print(f"----INVENTORY----\nPotions : {total_potion}\nShield : {total_shield}")
                continue

            elif action.upper() == "E": # Exit Single Battle
                
                print(f"Battle stats\nTotal Wins : {total_wins}")
                current_save = {"total_wins": total_wins,
                                        "inv": inv}
                
                with open("save_data.json", "w") as file:
                    json.dump(current_save, file, indent=4)
                print("Progress saved")
                break
            
            else: # For non-excepted input
                
                print("Invalid Input\n Try 'A'")
                continue

    elif primary_action == "2":
        
        print("----Welcome To Dungeon----\nDefeat all the three Monsters to win Dungeon battle")
        concern_action = input("\nEnter 1 to continue\nEnter 'E' to exit Dungeon\n----> ")

        if concern_action == "1":
            dungeon_cleared = True

            for room in range(1, 4):
                    
                current_enemy = random.choice(monster_pool).copy()
                print(f"----Battle Starts----\nYou are in room {room}\nCurrent Monster : {current_enemy['name']} (HP:{current_enemy['hp']})\n")
                                
                shield_is_active = False

                while hero_hp > 0 and current_enemy["hp"] > 0:
                    
                    if shield_is_active:
                        print("Shield activated")
                    else:
                        print("Choose your action")

                    action = input("-----------------\nEnter 'A' to HIT the Goblin\nEnter 'P' to use Portion\nEnter 'R' for rest \nEnter 'S' to activate shield \nEnter 'I' to inspect inventory\nEnter 'E to exit\n----> ")

                    if action.upper() == "A": # hero's attack
                        
                        if stamina > 10: # hero can attack
                            stamina = stamina - 15
                            dmg_to_monster, is_crt = dmg(10, 18, 20)
                            current_enemy["hp"] = current_enemy["hp"] - dmg_to_monster
                        
                            if current_enemy["hp"] <= 0:
                                print(f"You defeated {current_enemy['name']}")                                   
                                break
                            
                            if is_crt: # critical attack
                                print(f"BOOM!!, CRITICAL DEAlT 2x DAMAGE!!\n Damage Dealt {dmg_to_monster}\n {current_enemy['name']} Current HP : {current_enemy['hp']}")
                            else: # normal attack
                                print(f"You hitted goblin and dealt damge {dmg_to_monster}\n {current_enemy['name']} Current HP : {current_enemy['hp']}")
                        
                        else: # hero can't attack
                            print("You are out of stamina\nRest for a while (use 'R') : ")
                            continue

                        # Monster's attack
                        dmg_to_hero , is_crt = dmg(current_enemy["min_dmg"], current_enemy["max_dmg"], 10)
                        if shield_is_active:
                            dmg_to_hero = dmg_to_hero - 10
                            if dmg_to_hero <= 0:
                                dmg_to_hero = 0
                            shield_is_active = False
                        hero_hp = hero_hp - dmg_to_hero
                        
                        
                        if hero_hp <= 0: #Monster won
                            print(f"{current_enemy['name']} won , Try again ;)")
                            dungeon_cleared = False
                            break

                        else:
                            if is_crt: # Monster's critical attack
                                print(f"OOuch, {current_enemy['name']} Hitted You with a critical \n It dealt a damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")
                            else: # Monster's normal attack
                                print(f"{current_enemy['name']} Hitted you and dealt damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")

                    elif action.upper() == "P": # healing
                        item_used = use_item("potion")
                        
                        if not item_used:
                            continue

                        # Monster's attack
                        dmg_to_hero , is_crt = dmg(current_enemy["min_dmg"], current_enemy["max_dmg"], 10)
                        if shield_is_active:
                            dmg_to_hero = dmg_to_hero - 10
                            if dmg_to_hero <= 0:
                                dmg_to_hero = 0
                            shield_is_active = False
                        hero_hp = hero_hp - dmg_to_hero
                        
                        if hero_hp <= 0: #Monster won
                            print(f"{current_enemy['name']} won , Try again ;)")
                            dungeon_cleared = False
                            break
                        else:
                            if is_crt: # Monster's critical attack
                                print(f"OOuch, {current_enemy['name']} Hitted You with a critical \n It dealt a damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")
                            else: # Monster's normal attack
                                print(f"{current_enemy['name']} Hitted you and dealt damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")

                    elif action.upper() == "R": # stamina recovery
                        stamina = stamina + 25
                        
                        if stamina >= 50:
                            stamina = 50
                        print(f"You took a nap\n Your current stamina {stamina}")

                        # Monster's attack
                        dmg_to_hero , is_crt = dmg(current_enemy["min_dmg"], current_enemy["max_dmg"], 10)
                        if shield_is_active:
                            dmg_to_hero = dmg_to_hero - 10
                            if dmg_to_hero <= 0:
                                dmg_to_hero = 0
                            shield_is_active = False
                        hero_hp = hero_hp - dmg_to_hero
                        
                        if hero_hp <= 0: #Monster won
                            print(f"{current_enemy['name']} won , Try again ;)")
                        
                        else:
                            if is_crt: # Monster's critical attack
                                print(f"OOuch, {current_enemy['name']} Hitted You with a critical \n It dealt a damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")
                            else: # Monster's normal attack
                                print(f"{current_enemy['name']} Hitted you and dealt damage of {dmg_to_hero}\n Your Current HP : {hero_hp}")

                    elif action.upper() == "S": # shield activation with re-action chance

                        if use_item("shield"):
                            shield_is_active = True
                            continue
                        else:
                            continue
                                        
                    elif action.upper() == "I": # Display"s inventory items
                        
                        total_potion = inv.count("potion")
                        total_shield = inv.count("shield")
                        print(f"----INVENTORY----\nPotions : {total_potion}\nShield : {total_shield}")
                        continue

                    elif action.upper() == "E": # Exit Single Battle
                        
                        print(f"Battle stats\nTotal Wins : {total_wins}")
                        dungeon_cleared = False
                        break
                    
                    else: # For non-excepted input
                        
                        print("Invalid Input\n Try '1'")
                        continue

        if dungeon_cleared and hero_hp > 0:
            total_dungeon_wins = total_dungeon_wins + 1
            print(f"You cleared the dungeon\n Total dungeon Victorys : {total_dungeon_wins}")
            with open ("save_data.json", "w") as file:
                current_save = {"total_wins": total_wins, "total_dungeon_wins": total_dungeon_wins, "inv": inv}
                json.dump(current_save, file, indent=4)


    elif primary_action.upper() == "E": # Exit Game
        break
    
    else: # For non-excepted input
            
            print("Invalid Input\n Try '1'")
            continue


