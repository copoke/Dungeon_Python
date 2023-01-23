import time
import random
from ascii import *
from main import *
import sys
import copy

is_fighting = False
area = 1 #Ändrar beroende på 
inventorylist = []
def clear():
    print(chr(27) + "[2J")
def input_checker(value1, value2):
    while True:
        try:
            checked_input = int(input(">"))
            if checked_input >= value1 and checked_input <= value2:
                return checked_input
            else:
                print("Invalid Input")
                continue
        except ValueError:
            print("Invalid Input")
            continue
def class_selection():
    global character
    print("1. Bruiser 2. Tank 3. Assasin")
    chosen_class = input_checker(1, 3)
    if chosen_class == 1:
        character = Bruiser
    elif chosen_class == 2:
        character = Tank
    elif chosen_class == 3:
        character = Assasin
    time.sleep(1)
    print(f"You've chosen {character.Name}")
    return character
character = class_selection()
clear()
def print_list(list, is_count):
    counter = 1
    if is_count == False:
        for x in list:
            print(x)
    if is_count == True:
        for x in list:
            print(f"{counter}.{x}")
def health_bar_calculaton(type, printDamage):
    MAX_DASHES = 40
    convertion = type.MaxHP / MAX_DASHES   
    total_lines =  int(type.HP/convertion)
    hp_remaining = MAX_DASHES - total_lines

    line_string = "▆" * total_lines
    line_string_health = " " * hp_remaining
    entire_string = "|" + line_string + line_string_health + "|"
    if type == spawned_mob:
        if is_fighting == True:
            print(entire_string + "-" + str(character.DMG))
        else:
            print(entire_string)
    else:
        if is_fighting == True:
            print(entire_string + "-" + str(spawned_mob.DMG))
        else:
            print(entire_string)
def dialogue_spacing():
    print("----------------------------")
def EXP():
    character.EXP += spawned_mob.EXP_Drop
    if character.EXP >= character.MaxEXP:
        character.Level += 1
        character.EXP -= character.MaxEXP
        clear()
        for text in level_up_ascii:
            print(text)
            time.sleep(0.4)
            clear()
        print(level_up_full_ascii)
        time.sleep(3)
        card_selection()
    else:
        print(f"+ {spawned_mob.EXP_Drop} exp")
        dialogue_spacing()
        print(f"{character.EXP}/{character.MaxEXP} exp")
        print("\nPress enter to procced")
        input("")
def card_selection():
    clear()
    card_list = [Lethal_Precision,  Brutal_Momentum, Adept,  Swift_Foot, Health_Kit, Cursed_Weapon, Charged_Return, Thresher_Claws, Aggressive_Posture, Warriors_Respite]
    randomised_card_list = []
    looping = 0
    while looping < 3:
        random_card = random.randint(0,len(card_list) - 1)
        if looping == 0:
            randomised_card_list.append(card_list[random_card])
        else:
            if randomised_card_list.count(card_list[random_card]) < 1:
                randomised_card_list.append(card_list[random_card])
            else:
                looping -= 1
        looping += 1
    card_chooser(randomised_card_list, card_list)
def card_chooser(randomised_card_list, card_list):
    while True:
        print("Pick a card to view in detail:")
        dialogue_spacing()
        counter = 1
        for card in randomised_card_list:
            print(f"{counter}.{card.Name}")
            counter += 1
        dialogue_spacing()
        choose_card = int(input(">"))
        clear()
        print(randomised_card_list[choose_card -1].Name)
        dialogue_spacing()
        print(randomised_card_list[choose_card - 1].Description)
        print("\nAre you sure you want to pick this?")
        print("1. Yes 2. No")
        answer = input_checker(1, 2)
        if answer == 1:
            if randomised_card_list[choose_card - 1].Name != "Charged Return":
                add_stats(randomised_card_list, choose_card)
                card_list.remove(randomised_card_list[choose_card - 1])
                break
        clear()
def add_stats(chosen_cards, choose_card):
    character.DMG += chosen_cards[choose_card - 1].DMG
    character.Stamina += chosen_cards[choose_card - 1].Stamina
    character.HP += chosen_cards[choose_card - 1].HP
    character.Speed += chosen_cards[choose_card - 1].Speed
    character.Lifesteal  += chosen_cards[choose_card - 1].Lifesteal
    character.MaxEXP  += chosen_cards[choose_card - 1].MaxEXP
def mob_died():
    print(f"{spawned_mob.Name} died")
    dialogue_spacing()
    print(f"+ {spawned_mob.Drop}\n+ {spawned_mob.Coin_Drop} coins")
    EXP()
    inventorylist.append(spawned_mob.Drop)
    character.Coins  += spawned_mob.Coin_Drop
def mob_spawn_randomizer(moblist):
        global spawned_mob
        spawned_mob = copy.copy(random.choice(moblist))
        return spawned_mob.Name
def mob_spawn():
    mob_list_area_1 = [Zombie, Slime, Goblin]

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
    global is_fighting
    is_fighting = False
    print(fight_ascii)
    time.sleep(1)
    print(f"A {spawned_mob.Name} appears.")
    time.sleep(1)
    print ("What is your next action?")
    time.sleep(2)
    clear()
def fight_menu():
    global is_fighting
    print(f"{spawned_mob.Name} has {spawned_mob.HP}/{spawned_mob.MaxHP} Health")
    health_bar_calculaton(spawned_mob, is_fighting)
    print(f"You have {character.HP}/{character.MaxHP} Health")
    health_bar_calculaton(character, is_fighting)
    dialogue_spacing()
    print("1.Fight 2.Run 3.Inventory 4.Stats")
    choosen_action = input_checker(1, 4)
    if choosen_action == 1:
        hit()
        is_fighting = True
    elif choosen_action == 2:
        run()
        is_fighting = False
    elif choosen_action == 3:
        inventory()
        is_fighting = False
    elif choosen_action == 4:
        stats()
        print("\nPress enter to proceed" )
        input("")
        is_fighting = False
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


#Working Damage indicators on health bars, Mob spawning multiple  times, Skills(Temporary damage multiplier), if time avaible status effects