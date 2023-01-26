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
def health_bar_calculaton(type):
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
    global area
    next_area = 3 #ToDo: Resettar next area, kommer alltid vara 3
    character.EXP += spawned_mob.EXP_Drop
    if character.EXP >= character.MaxEXP:
        character.Level += 1
        character.EXP -= character.MaxEXP
        character.MaxEXP *= 1.3
        character.MaxHP += 10
        character.HP += 5
        if character.Level >= next_area:
            for text in new_area_ascii:
                clear()
                print(text)
                time.sleep(0.3)
                clear()
            clear()
            print(full_area_ascii)
            time.sleep(1)
            next_area += 3
            area += 1
            character.HP = character.MaxHP
            character.Stamina = character.Stamina
        clear()
        time.sleep(1)
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
        print(f"{character.EXP}/{int(character.MaxEXP)} exp")
        print("\nPress enter to procced")
        input("")
def card_selection():
    clear()
    randomised_card_list = []
    looping = 0
    while looping < 3:
        random_card = random.choice(card_list)
        if looping == 0:
            randomised_card_list.append(random_card)
        else:
            if randomised_card_list.count(random_card) < 1:
                randomised_card_list.append(random_card)
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
        choose_card = input_checker(1, len(randomised_card_list)) - 1
        clear()
        print(randomised_card_list[choose_card].Name)
        dialogue_spacing()
        print(randomised_card_list[choose_card].Description)
        print("\nAre you sure you want to pick this?")
        print("1. Yes 2. No")
        answer = input_checker(1, 2)
        if answer == 1:
            if randomised_card_list[choose_card].Name != "Charged Return":
                card_list.remove(randomised_card_list[choose_card])
                add_stats(randomised_card_list, choose_card)
                break
        clear()
def add_stats(chosen_cards, choose_card):
    character.DMG += chosen_cards[choose_card].DMG
    character.Stamina += chosen_cards[choose_card].Stamina
    character.HP += chosen_cards[choose_card].HP
    character.Speed += chosen_cards[choose_card].Speed
    character.Lifesteal  += chosen_cards[choose_card].Lifesteal
    character.MaxEXP  += chosen_cards[choose_card].MaxEXP
def move_selection():
    options_move_list = []
    dialogue_spacing()
    for move in move_list:
        if move.Level <= character.Level:
            options_move_list.append(move)
    while True:
        print("Pick a move to view in detail")
        dialogue_spacing()
        print_list(options_move_list, True)
        dialogue_spacing()
        move_input = input_checker(1, len(options_move_list)) - 1
        clear()
        print({options_move_list[move_input].Name})
        dialogue_spacing()
        print(f"\n{options_move_list[move_input].Description}")
        print("Are you sure you want to choose this?")
        move_input_selection = input_checker(1, 2)
        if move_input_selection == 1:
            character_move_list.append(options_move_list[move_input])
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
    clear()
def fight_menu():
    global is_fighting
    if character.HP > character.MaxHP:
        character.HP = character.MaxHP
    print(f"{spawned_mob.Name} has {spawned_mob.HP}/{spawned_mob.MaxHP} Health")
    health_bar_calculaton(spawned_mob)
    print(f"You have {character.HP}/{character.MaxHP} Health")
    health_bar_calculaton(character)
    dialogue_spacing()
    print("1.Fight? 2.Run? 3.Inventory? 4.Stats?")
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
        is_fighting = False
        print("\nPress enter to proceed" )
        input("")
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
    if character.Stamina <= character.MaxStamina -2:
        character.Stamina += 2
    if len(character_move_list) == 0 or character.Stamina <= 0:
        if character.Speed < spawned_mob.Speed:
            character.HP -= spawned_mob.DMG
            if character.HP <= death:
                time.sleep(1)
                print("You've been killed.")
                time.sleep(2)
                sys.exit
            spawned_mob.HP -= character.DMG
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
        print_list(character_move_list, True)
def fighting():
    mob_spawn()
    fight_intro()
    while character.HP > 0 and spawned_mob.HP > 0:
        fight_menu()
def inventory():
    global inventorylist
    #Inventory prints multiple of same item
    clear()
    print(f"{character.Coins} Coins")
    dialogue_spacing()
    accounted_items = []
    for owned_item in inventorylist:
        item_counter = inventorylist.count(owned_item)
        if item_counter > 1 and accounted_items.count(owned_item) < 1:
            plural_checker = plural_list.count(owned_item)
            if plural_checker == 0:
                print(f"{item_counter} {owned_item}")
                accounted_items.append(owned_item)
            else:
                print(f"{item_counter} {owned_item}'s")
        elif accounted_items.count(owned_item) < 1:
            print(f"{item_counter} {owned_item}")
            accounted_items.append(owned_item)
        item_counter = 0
    dialogue_spacing()
    if len(character_move_list) > 0:
        print("Your Moves:")
        dialogue_spacing()
        print_list(character_move_list, False)
    print("Press enter to proceed")
    input()
while True:
    fighting()


#Working Damage indicators on health bars, Mob spawning multiple  times, Skills(Temporary damage multiplier), if time avaible status effects