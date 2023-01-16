import time
import random
from ascii import *
from main import *
import sys
import pprint
area = 1 #Ändrar beroende på 

def clear():
    print(chr(27) + "[2J")

def class_selection():
    print("1.Bruiser 2.Tank 3.Assasin")
    chosen_class = int(input(">"))
    if chosen_class == 1:
        character = Bruiser
    elif chosen_class == 2:
        character = Tank
    elif chosen_class == 3:
        character = Assasin
    else:
        print("Invalid Input")
    time.sleep(1)
    print(f"You've chosen {character.Name}")
    return character
character = class_selection()
time.sleep(1)
clear()

def dialogue_spacing():
    print("----------------------------")
def EXP():
    character.EXP += spawned_mob.EXP_Drop
    print(f"You got {spawned_mob.EXP_Drop} exp")
    if character.EXP >= character.MaxExp:
        character.Level += 1
        print("You leveled up!")    
    print(f"You now have {character.EXP}/{character.MaxExp} exp.")

def mob_died():
    time.sleep(1)
    print(f"The {spawned_mob.Name} died")
    time.sleep(2)
    EXP()
    print(f"You got {spawned_mob.Drop} and {spawned_mob.Coin_Drop} coins")
    print("\nPress enter to procced")
    input("")
    mob_spawn()

def mob_spawn_randomizer(moblist):
        global spawned_mob
        random_spawn = random.randint(0,len(moblist) - 1)
        spawned_mob = moblist[random_spawn]
        return spawned_mob.Name
def mob_spawn():
    if area == 1:
        mob_name = mob_spawn_randomizer(mob_list_area_1)
    elif area == 2:
        mob_name = mob_spawn_randomizer(mob_list_area_2)
    elif area == 3:
        mob_name = mob_spawn_randomizer(mob_list_area_3)
    return mob_name
def fight_intro():
    mob_spawn()
    print("A battle has begun!")
    time.sleep(1)
    print(f"A {spawned_mob.Name} appears.")
    time.sleep(1)
    print ("What is your next action?")
    time.sleep(2)
    clear()
def fight_menu():
    print(f"{spawned_mob.Name} has {spawned_mob.HP}/{spawned_mob.MaxHP} Health")
    print(f"You have {character.HP}/{character.MaxHP} health")
    dialogue_spacing()
    print("1.Fight? 2.Run? 3.Inventory? 4.Stats?")
    choosen_action = int(input(">"))
    if choosen_action == 1:
        hit()
    elif choosen_action == 2:
        run()
    elif choosen_action == 3:
        inventory()
    elif choosen_action == 4:
        stats()
        print("\nPress enter to proceed" )
        input("")
    else:
        print("Invalid Input")
    clear()
def stats():
    clear()
    print(f"HP: {character.HP}/{character.MaxHP}")
    print(f"Damage: {character.DMG}")
    print(f"Speed: {character.Speed}")
    print(f"EXP: {character.EXP}/{character.MaxExp}")
    print(f"Level: {character.Level}")
def run():
    print ("You chose run.")
    run_chance = random.randint(1,3)
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(1)
    if run_chance == 3:
        print("You succesfully fled, you live to fight another day.")
    if run_chance < 3:
        print("You failed to run")
        character.HP -= spawned_mob.DMG
        if character.HP > 0:
            print("Returning to battle")
def hit():
    death = 0
    if character.Speed < spawned_mob.Speed:
        character.HP -= spawned_mob.DMG
        time.sleep(1)
        print(f"{spawned_mob.Name} hit you for {spawned_mob.DMG} damage")
        time.sleep(1)
        if character.HP <= death:
            time.sleep(1)
            print("You've been killed.")
            time.sleep(2)
            sys.exit
        else:
            spawned_mob.HP -= character.DMG
            print(f"You've done {character.DMG} damage to {spawned_mob.Name}, it now has {spawned_mob.HP}/{spawned_mob.MaxHP} Health")
            time.sleep(1)
        if spawned_mob.HP <= death:
            clear()
            mob_died()
    elif character.Speed >= spawned_mob.Speed:
        spawned_mob.HP -= character.DMG
        time.sleep(1)
        if spawned_mob.HP <= death:
            spawned_mob.HP = 0
        print(f"You've done {character.DMG} damage to {spawned_mob.Name}, it now has {spawned_mob.HP}/{spawned_mob.MaxHP} Health")
        time.sleep(1)
        if spawned_mob.HP > 0:
            character.HP -= spawned_mob.DMG
            print(f"{spawned_mob.Name} hit you for {spawned_mob.DMG} damage, you now have {character.HP}/{character.MaxHP} Health")
            time.sleep(2)
            if character.HP <= death:
                time.sleep(1)
                print("You've been killed.")
                sys.exit
        else:
            clear()
            mob_died()
def inventory():
    for item in mob_drop_list:
        if item > 0:
            print(f"{item}")
def fighting():
    fight_intro()
    while character.HP > 0 and spawned_mob.HP > 0:
        fight_menu()
while True:
    fighting()





#inventory, mob drops