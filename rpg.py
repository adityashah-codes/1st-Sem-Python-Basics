import random
# variables
player_hp = 100
goblin_hp = 50
portions = 3
# damge dealer
def dmg(min, max):
    hit = random.randint(min, max)
    return hit
# portion dealer
def heal():
    global player_hp, portions
    if portions > 0:
        heal_amt = 25
        player_hp = player_hp + heal_amt
        portions = portions - 1
        if  player_hp > 100:
            player_hp = 100
        print(f"You used 1 portion \n current HP {player_hp}")
    else:
        print("You ran out of portions")
# battle loop
while player_hp > 0 and goblin_hp > 0:
    print("----BATTLE BEGINS----")
    action = input("Enter 'A' to HIT the GOblin\nEnter 'P' to use Portion \n----> ")
    if action.upper() == "A":
        dmg_to_gob = dmg(10, 18)
        goblin_hp = goblin_hp - dmg_to_gob
        print(f"You hitted goblin : {dmg_to_gob}\nGoblin's Current HP : {goblin_hp} ")
        if goblin_hp <= 0:
            print("YOU DEFEATED GOBLIN")
            break
        else:
            dmg_to_ply = dmg(3, 12)
            player_hp = player_hp - dmg_to_ply
            print(f"Goblin Bites you : {dmg_to_ply}\n Your current Health : {player_hp}")
        if player_hp <= 0:
            print("Goblin defeated you")
            break
    elif action.upper() == "P":
        heal()
        print(f"You have {portions} left")
        dmg_to_ply = dmg(3, 12)
        player_hp = player_hp - dmg_to_ply
        print(f"Goblin Bites you : {dmg_to_ply}\n Your current Health : {player_hp}")
    else:
        print("INvalid Move")

    
    