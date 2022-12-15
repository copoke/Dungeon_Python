import time
import random
import main
import ascii


def fighting():
    print("{} has {}/{} health".format(mob_name, mob_health, mob_health))
    time.sleep(1)
    print("What is your next action?")
    time.sleep(1)
    while True:
        time.sleep(1)
        print("1.Fight? 2.Run? 3.Heal? 4.Inventory")
        try:
            player_choice = int(input(">"))
        except ValueError or player_choice > 4:
            print("Wrong input")
            continue
        if player_choice == PLAYER_RUNS:
            print("You chose run.")
            chance_to_run = random.randint(1, 3)
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            print("...")
            time.sleep(1)
            if chance_to_run == 3:
                print("You succesfully fled, you live to fight another day")
                break
            if chance_to_run < 3:
                print("You failed to flee, returning to battle.")
        if player_choice == PLAYER_FIGHTS:
            print("You chose fight, you did {} damage".format(player_damage))
            mob_health = mob_health - player_damage
            time.sleep(1)
            if mob_health <= 0:
                print("You killed the {}".format(mob_name))
            else:
                print("The {} now has {} health remaining".format(
                    mob_name, mob_health))
        if player_choice == PLAYER_HEALS:
            player_health = player_health + healingamount
            if player_health > player_maxhp:
                player_health = player_maxhp
            print("You've healed for {} health, you now have {}/{}".format(
                healingamount, player_health, player_maxhp))
        if player_choice == PLAYER_INVENTORY:
            print("-------")
            inventoryopen()
            print("-------")
        if player_choice != PLAYER_HEALS and player_choice != PLAYER_INVENTORY and player_choice != PLAYER_RUNS and player_choice != PLAYER_FIGHTS:
            print("Invalid action")
            invalid_choice = 1
        if player_health <= player_dead:
            print("You've died!")
            sys.exit()
        saved_health = player_health
        if mob_health > MOB_ALIVE and player_choice != PLAYER_INVENTORY and invalid_choice != 1:
            player_health = player_health - mob_damage
            time.sleep(1)
            print("The {} did {} damage to you".format(mob_name, mob_damage))
            time.sleep(2)
            print("You now have {}/{} health left".format(player_health, player_maxhp))
        if mob_health <= MOB_DEAD:
            player_restamount = player_maxrest
            mobdrop()
            time.sleep(1)
            print("+{} coins".format(coin_number))
            time.sleep(1)  # 70 --> 63
            if exp_total < required_exp and mob_health <= MOB_DEAD:
                print("{}/{} experience".format(exp_total, required_exp))
                time.sleep(0.5)
            if exp_total >= required_exp:
                level += 1
                print(f"You have reached level {level}")
                player_health = player_maxhp
                required_exp = required_exp * 1.1
                exp_total = 0
                time.sleep(1)
            break