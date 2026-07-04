import random
# variables
player_hp = 100
stamina = 50
goblin_hp = 50
portions = 3
# functions
def dmg(min, max, crt):
    hit = random.randint(min, max)
    if random.randint(1, 100) == crt:
        hit = hit*2
        return hit, True
    return hit, False
def heal():
    global player_hp, portions
    if portions > 0:
        heal_amt = 25
        player_hp = player_hp + heal_amt
        portions = portions - 1
        if  player_hp > 100:
            player_hp = 100
        print(f"You used 1 portion \n current HP {player_hp}")
        print(f"You have {portions} left")
    else:
        print("You ran out of portions")
# battle loop
while player_hp > 0 and goblin_hp > 0:
    print("----BATTLE BEGINS----")
    action = input("Enter 'A' to HIT the GOblin\nEnter 'P' to use Portion\nEnter 'R' for rest \n----> ")
    if action.upper() == "A": # hero's attack
        if stamina > 10: # hero can attack
            stamina = stamina - 15
            dmg_to_gob, is_crt = dmg(10, 18, 20)
            goblin_hp = goblin_hp - dmg_to_gob
            if is_crt: # critical attack
                print(f"BOOM!!, CRITICAL DEAlT 2x DAMAGE!!\n Damage Dealt {dmg_to_gob}\n Goblins Current HP : {goblin_hp}")
            else: # normal attack
                print(f"You hitted goblin and dealt damge {dmg_to_gob}\n Goblins Current HP : {goblin_hp}")
        else:
            print("You are out of stamina\nRest for a while (use 'R') : ")
        # goblin's attack
        dmg_to_hero , is_crt = dmg(5, 12, 10)
        player_hp = player_hp - dmg_to_hero
        if player_hp <= 0:
            print("Goblin won , Try again ;)")
        else:
            if is_crt: # goblin's critical attack
                print(f"OOuch, Goblin Hitted You with a critical \n It dealt a damage of {dmg_to_hero}\n Your Current HP : {player_hp}")
            else: # goblin's normal attack
                print(f"Goblin Hitted you and dealt damage of {dmg_to_hero}\n Your Current HP : {player_hp}")
    elif action.upper() == "P": # healing
        heal()
        # goblin's attack
        dmg_to_hero , is_crt = dmg(5, 12, 10)
        player_hp = player_hp - dmg_to_hero
        if player_hp <= 0:
            print("Goblin won , Try again ;)")
        else:
            if is_crt: # goblin's critical attack
                print(f"OOuch, Goblin Hitted You with a critical \n It dealt a damage of {dmg_to_hero}\n Your Current HP : {player_hp}")
            else: # goblin's normal attack
                print(f"Goblin Hitted you and dealt damage of {dmg_to_hero}\n Your Current HP : {player_hp}")
    elif action.upper() == "R": # stamina recovery
        stamina = stamina + 25
        if stamina >= 50:
            stamina = 50
        print(f"You took a nap\n Your current stamina {stamina}")
        # goblin's attack
        dmg_to_hero , is_crt = dmg(5, 12, 10)
        player_hp = player_hp - dmg_to_hero
        if player_hp <= 0:
            print("Goblin won , Try again ;)")
        else:
            if is_crt: # goblin's critical attack
                print(f"OOuch, Goblin Hitted You with a critical \n It dealt a damage of {dmg_to_hero}\n Your Current HP : {player_hp}")
            else: # goblin's normal attack
                print(f"Goblin Hitted you and dealt damage of {dmg_to_hero}\n Your Current HP : {player_hp}")
    else:
        print("Invalid Input\n Try 'A'")


