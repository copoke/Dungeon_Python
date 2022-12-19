import time
import random
from ascii import *
from main import *
area = 1 #Ändrar beroende på Area
def mob_spawn_randomizer(moblist):
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


def fight_dialogue():
    mob_name = mob_spawn()
    print("A battle has begun!")
    time.sleep(1)
    print(f"A {mob_name} appears.")
    time.sleep(1)
    print ("What is your next action?")
    time.sleep(1)
def fighting():
    fight_dialogue()

fighting()