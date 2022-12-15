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

Katana = Weapon("Katana", 6, 6, 30, 8, 0)

Crucible_rapier = Weapon("Crucible Rapier", 5, 7, 30, 13, 1)

#Tier 3
Longbow = Weapon("Longbow",12, 2, 40, 5, 0)

Spear = Weapon("Spear", 14, 2, 35, 4, 0)

Axe = Weapon("Axe",13 ,4 ,45 ,6 ,4 )

#Tier 4
Halberd = Weapon("Halberd", 18, 1, 50, 7, 2)

Leviathan = Weapon("Leviathan", 16, 3, 55, 8, 5)

Blades_of_chaos= Weapon("Blades of Chaos", 15, 5, 55, 10, 4)

#Tier 5 
Excalibur = Weapon("Excalibur", 23, 4, 85, 14, 14)

Mjölnir = Weapon("Mjönir", 28, 2, 80, 8, 8)

Lightsaber = Weapon ("Lightsaber", 26, 3, 70, 16, 6)




