import time
import random
from ascii import *
from main import *
import sys
import copy

is_fighting = False
area = 1
inventorylist = []
def clear():
    print(chr(27) + "[2J")
def input_checker(value1, value2): #Tar upp 2 värden och accepterar input mellan det, returnerar din input
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
def spawn_boss(boss):
    global spawned_mob
    print("You find a stronger sword making ur damage significantly higher, aswell as finding boots on the ground")
    character.MaxHP += 20
    character.DMG += 5
    print("A boss approaches")
    time.sleep(3)
    character.HP = character.MaxHP
    spawned_mob = boss
def print_names(list): #Printar objects namn istället för själva objectet
    counter = 1
    for object in list:
        print(f"{counter}.{object.Name}")
        counter += 1
def print_list(list, is_count): #Printar lista beroende på om du ska räkna eller inte räkna
    counter = 1
    if is_count == False:
        for x in list:
            print(x)
    if is_count == True:
        for x in list:
            print(f"{counter}.{x}")
            counter += 1
def health_bar_calculaton(type): #Matte för health bars, använder type för att ta upp antingen character eller spawned_mob instancerna
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
            if character.Lifesteal > spawned_mob.DMG:
                print(entire_string + "+" + str(character.Lifesteal - spawned_mob.DMG))
            elif character.Lifesteal == spawned_mob.DMG:
                print(entire_string)
            else:
                print(entire_string + "-" + str(spawned_mob.DMG))
        else:
            print(entire_string)
def dialogue_spacing():
    print("----------------------------")
def EXP(): #Simpel funktion som blir kallad varje gång du dödar ett mob, exp gain
    global area
    character.EXP += spawned_mob.EXP_Drop
    if character.EXP >= character.MaxEXP:
        character.Level += 1
        character.EXP -= character.MaxEXP
        character.MaxEXP *= 1.3
        character.MaxHP += 10
        character.HP += 5
        if character.Level == 3:
            new_area()
        elif character.Level == 6:
            new_area()
        clear()
        time.sleep(1)
        for text in level_up_ascii:
            print(text)
            time.sleep(0.4)
            clear()
        print(level_up_full_ascii)
        time.sleep(3)
        character.HP = character.MaxHP
        card_selection()
        time.sleep(0.5)
        move_selection()
    else:
        print(f"+ {spawned_mob.EXP_Drop} exp")
        dialogue_spacing()
        print(f"{character.EXP}/{int(character.MaxEXP)} exp")
        print("\nPress enter to procced")
        input("")
def new_area():
    global area
    global spawned_mob
    for text in new_area_ascii:
        clear()
        print(text)
        time.sleep(0.3)
        clear()
    clear()
    print(full_area_ascii)
    time.sleep(1)
    area += 1
    if area == 2:
       spawn_boss(Gromp)
    elif area == 3:
        spawn_boss(Dragon)
    character.HP = character.MaxHP
    character.Stamina = character.Stamina
def card_selection():
    clear()
    randomised_card_list = []
    looping = 0
    while looping < 3: #Randomisar ett kort och adderar det till en lista, kollar om kortet redan finns om det gör det kommer den loopa igen
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
def card_chooser(randomised_card_list, card_list): #Visuell meny  för att välja kort
    while True:
        print("Pick a card to view in detail:")
        dialogue_spacing()
        print_names(randomised_card_list)
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
            card_list.remove(randomised_card_list[choose_card]) #Tar bort kortet från card_list
            add_stats(randomised_card_list, choose_card) #Adderar alla stats du får från korten
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
    clear()
    for move in move_list:
        if move.Level <= character.Level:
            options_move_list.append(move)
    while True:
        print("Pick a move to view in detail")
        dialogue_spacing()
        print_names(options_move_list)
        dialogue_spacing()
        move_input = input_checker(1, len(options_move_list)) - 1
        clear()
        print(f"{options_move_list[move_input].Name}")
        dialogue_spacing()
        print(f"{options_move_list[move_input].Description}")
        print("\nAre you sure you want to choose this?")
        print("1. Yes 2. No")
        move_input_selection = input_checker(1, 2)
        if move_input_selection == 1:
            character_move_list.append(options_move_list[move_input])
            move_list.remove(options_move_list[move_input])
            break
        clear()
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
    if character.Stamina <= character.Stamina - 2:
        character.Stamina += 2
    print(f"{spawned_mob.Name} has {spawned_mob.HP}/{spawned_mob.MaxHP} Health")
    health_bar_calculaton(spawned_mob)
    print(f"You have {character.HP}/{character.MaxHP} Health")
    health_bar_calculaton(character)
    dialogue_spacing()
    print("1.Fight? 2.Moves? 3.Run? 4.Inventory? 5.Stats?")
    choosen_action = input_checker(1, 5)
    if choosen_action == 1:
        hit()
        is_fighting = True
    elif choosen_action == 2:
        skill()
        clear()
        is_fighting = False
    elif choosen_action == 3:
        run()
        is_fighting = False
    elif choosen_action == 4:
        inventory()
        is_fighting = False
    elif choosen_action == 5:
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
    character.HP += character.Lifesteal
def skill():
    if len(character_move_list) > 0:
        print("Pick a move to use:")
        dialogue_spacing()
        print_names(character_move_list)
        dialogue_spacing()
        chosen_move = input_checker(1, len(character_move_list)) - 1
        if character.Stamina + character_move_list[chosen_move].Cost < 0:
            print("You do not have enough stamina")
            time.sleep(1)
        else:
            player_stat_change(chosen_move)
            mob_stat_change(chosen_move)
    else:
        print("You have no moves.")
        time.sleep(1)
def player_stat_change(index):
    character.HP += character_move_list[index].HP
    character.Stamina += character_move_list[index].Cost
    character.Lifesteal += character_move_list[index].Lifesteal
def mob_stat_change(index):
    if character.Speed + character_move_list[index].Speed < spawned_mob.Speed:
        character.HP -= spawned_mob.DMG
        if character.HP <= 0:
            sys.exit
        spawned_mob.HP -= character.DMG + character_move_list[index].DMG
        if spawned_mob.HP <= 0:
            clear()
            mob_died()
    else:
        spawned_mob.HP -= character.DMG + character_move_list[index].DMG
        if spawned_mob.HP <= 0:
            clear()
            mob_died()
        character.HP -= spawned_mob.DMG
        if character.HP <= 0:
            sys.exit
def fighting():
    if character.HP > 0:
        mob_spawn()
        fight_intro()
    else:
        print("Game Over!")
        sys.exit
    while character.HP > 0 and spawned_mob.HP > 0:
        fight_menu()
def inventory():
    global inventorylist
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