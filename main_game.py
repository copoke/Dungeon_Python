import time
import random
from ascii import *
from main import *
import sys
area = 1 #Ändrar beroende på 
inventorylist = []
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
def print_list(list, is_count):
    counter = 1
    if is_count == False:
        for x in list:
            print(x)
    if is_count == True:
        for x in list:
            print(f"{counter}.{x}")
def health_bar_calculaton(type):
    MAX_DASHES = 40
    convertion = type.MaxHP / MAX_DASHES   
    total_lines =  int(type.HP/convertion)
    hp_remaining = MAX_DASHES - total_lines

    line_string = "▆" * total_lines
    line_string_health = " " * hp_remaining
    if type == spawned_mob:
        print ("|" + line_string + line_string_health + "| -" +  str(character.DMG))
    elif type == character:
        print ("|" + line_string + line_string_health + "| -" +  str(spawned_mob.DMG))
    else:
        print ("|" + line_string + line_string_health + "|")
def dialogue_spacing():
    print("----------------------------")
def EXP():
    character.EXP += spawned_mob.EXP_Drop
    print(f"You got {spawned_mob.EXP_Drop} exp")
    if character.EXP >= character.MaxEXP:
        character.Level += 1
        character.EXP -= character.MaxEXP
        print("You leveled up!")
        time.sleep(2)
        card_selection()
    print(f"You now have {character.EXP}/{character.MaxEXP} exp.")
def card_selection():
    clear()
    chosen_cards = []
    answer = 0
    looping = 0
    dialogue_spacing()
    while looping < 3:
        random_card = random.randint(0,len(Card_List) - 1)
        if looping == 0:
            chosen_cards.append(Card_List[random_card])
        else:
            if chosen_cards.count(Card_List[random_card]) < 1:
                chosen_cards.append(Card_List[random_card])
            else:
                looping -= 1
        looping += 1
    while True:
        counter = 1
        for card in chosen_cards:
            print(f"{counter}.{card.Name}")
            counter += 1
        dialogue_spacing()
        choose_card = int(input(">"))
        clear()
        print(chosen_cards[choose_card -1].Name)
        dialogue_spacing()
        print(chosen_cards[choose_card - 1].Description)
        print("\nAre you sure you want to pick this?")
        print("1. Yes 2. No")
        answer = int(input(">"))
        if answer == 1:
            if chosen_cards[choose_card - 1].Name != "Charged Return":
                add_stats(chosen_cards, choose_card)
                Card_List.remove(chosen_cards[choose_card - 1])
                break
        clear()
def add_stats(chosen_cards, choose_card):
    character.DMG += chosen_cards[choose_card].DMG
    character.Stamina += chosen_cards[choose_card].Stamina
    character.HP += chosen_cards[choose_card].HP
    character.Speed += chosen_cards[choose_card].Speed
    character.Lifesteal  += chosen_cards[choose_card].Lifesteal
    character.MaxEXP  += chosen_cards[choose_card].MaxEXP
def mob_died():
    print(f"The {spawned_mob.Name} died")
    print(f"You got {spawned_mob.Drop} and {spawned_mob.Coin_Drop} coins")
    print("\nPress enter to procced")
    input("")
    EXP()
    inventorylist.append(spawned_mob.Drop)
    character.Coins  += spawned_mob.Coin_Drop
def mob_spawn_randomizer(moblist):
        global spawned_mob
        random_spawn = random.randint(0,len(moblist) - 1)
        spawned_mob = moblist[random_spawn]
        return spawned_mob.Name
def mob_spawn():
    mob_list_area_1 = [Slime, Zombie, Goblin]

    mob_list_area_2 = [Skeleton, Spider, Wolf]

    mob_list_area_3 = [Golem, Gargoyle, Ogre, Snake]
    if area == 1:
        mob_name = mob_spawn_randomizer(mob_list_area_1)
    elif area == 2:
        mob_name = mob_spawn_randomizer(mob_list_area_2)
    elif area == 3:
        mob_name = mob_spawn_randomizer(mob_list_area_3)
    return mob_name
def fight_intro():
    print(fight_ascii)
    time.sleep(1)
    print(f"A {spawned_mob.Name} appears.")
    time.sleep(1)
    print ("What is your next action?")
    time.sleep(2)
    clear()
def fight_menu():
    print(f"{spawned_mob.Name} has {spawned_mob.HP}/{spawned_mob.MaxHP} Health")
    health_bar_calculaton(spawned_mob)
    print(f"You have {character.HP}/{character.MaxHP} Health")
    health_bar_calculaton(character)
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
    print(f"EXP: {character.EXP}/{character.MaxEXP}")
    print(f"Stamina: {character.Stamina}/{character.MaxStamina}")
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
            time.sleep(1)
            print("Returning to battle")
            time.sleep(1)
def hit():
    death = 0
    if len(Total_Moves) == 0 or character.Stamina <= 0:
        if character.Speed < spawned_mob.Speed:
            character.HP -= spawned_mob.DMG
            if character.HP <= death:
                time.sleep(1)
                print("You've been killed.")
                time.sleep(2)
                sys.exit
            if spawned_mob.HP <= death:
                spawned_mob.HP = 0
                clear()
                mob_died()
        elif character.Speed >= spawned_mob.Speed:
            spawned_mob.HP -= character.DMG
            if spawned_mob.HP <= death:
                spawned_mob.HP = 0
                clear()
                mob_died()
            if spawned_mob.HP > 0:
                character.HP -= spawned_mob.DMG
            if character.HP <= death:
                time.sleep(1)
                print("You've been killed.")
                sys.exit
    else:
        print_list(Total_Moves, True)
def fighting():
    mob_spawn()
    fight_intro()
    while character.HP > 0 and spawned_mob.HP > 0:
        fight_menu()
def inventory():
    global inventorylist
    clear()
    print(f"{character.Coins} Coins")
    dialogue_spacing()
    for owned_item in inventorylist:
        item_counter = inventorylist.count(owned_item)
        if item_counter > 1:
            plural_checker = plural_list.count(owned_item)
            if plural_checker == 0:
                print(f"{item_counter} {owned_item}")
            else:
                print(f"{item_counter} {owned_item}'s")
        else:
            print(f"{item_counter} {owned_item}")
        item_counter = 0
    dialogue_spacing()
    if len(Total_Moves) > 0:
        print("Your Moves")
        dialogue_spacing()
        print_list(Total_Moves, False)
    print("Press enter to proceed")
    input()
while True:
    fighting()





#Working Damage indicators on health bars