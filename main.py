class Mobs:
    def __init__(self, HP, MaxHP, DMG, Speed):
        self.HP = HP
        self.MaxHP = MaxHP
        self.DMG = DMG
        self.Speed = Speed
class Player:
    def __init__(self, HP, MaxHP, DMG, Speed, EXP, MaxEXP, Heal, Run_Chance):
        self.HP = HP
        self.MaxHP = MaxHP
        self.DMG = DMG
        self.Speed = Speed
        self.EXP = EXP
        self.MaxExp = MaxEXP
        self.Heal = Heal
        self.Run_chance = Run_Chance
class Armor:
    def __init__(self, Durability, Def, Weight, HP):
        self.Durability = Durability
        self.Def = Def
        self.Weight = Weight
        self.HP = HP
class Weapon:
    def __init__(self, Name, DMG, Bleed, Durability, Speed, Lifesteal):
        self.Name = Name
        self.DMG = DMG
        self.Bleed = Bleed
        self.Durability = Durability
        self.Speed = Speed
        self.Lifesteal = Lifesteal

#Tier 1
Zweihänder = Weapon("Zweihänder", 8, 2, 15, -4, 0)

Scimitar = Weapon("Scimitar", 4, 4, 20, 6, 0)

Rapier = Weapon("Rapier", 3, 4, 25, 10, 0)

#Tier 2
Greatsword = Weapon("Greatsword", 10, 2, 32, -6, 0)

Katana = Weapon("Katana", 5, 6, 30, 8, 0)

Crucible_rapier = Weapon("Crucible Rapier", 5, 7, 30, 15, 1)



