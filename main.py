import gc
class Mob:
    def __init__(self, Name, HP, MaxHP, DMG, Speed, EXP_Drop, Drop, Coin_Drop):
        self.HP = HP
        self.Name = Name
        self.MaxHP = MaxHP
        self.DMG = DMG
        self.Speed = Speed
        self.EXP_Drop = EXP_Drop
        self.Drop = Drop
        self.Coin_Drop = Coin_Drop
class Player:
    def __init__(self, Name, HP, MaxHP, DMG, Speed, EXP, MaxEXP, Level, Coins, Stamina, MaxStamina, Lifesteal):
        self.HP = HP
        self.Name = Name
        self.MaxHP = MaxHP
        self.DMG = DMG
        self.Speed = Speed
        self.EXP = EXP
        self.MaxEXP = MaxEXP
        self.Level = Level
        self.Coins = Coins
        self.Stamina = Stamina
        self.MaxStamina = MaxStamina
        self.Lifesteal = Lifesteal
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
class Card:
    def __init__(self, Name, Description, Stamina, HP, Speed, DMG, Lifesteal, MaxEXP):
        self.Description = Description
        self.Stamina = Stamina
        self.HP = HP
        self.Speed = Speed
        self.Lifesteal = Lifesteal
        self.MaxEXP = MaxEXP
        self.DMG = DMG
        self.Name = Name
#Player classes
Bruiser = Player("Bruiser", 25, 25, 3, 3, 0, 40, 1, 0, 10, 10, 0)

Tank = Player("Tank", 30, 30, 2, 1, 0, 100, 1, 0, 5, 5, 0)

Assasin = Player("Assasin", 20, 20, 4, 4, 0, 100, 1, 0, 20, 20, 0)

#Player Cards
Lethal_Precision = Card("Lethal Precision", "You gain more precision in your attacks, making your hits land with greater strength", 1, 0, 0, 1, 0, 0)
Brutal_Momentum = Card("Brutal Momentum", "With every swing you keep your momentum, giving you more speed in your hits", 0, 0, 2, 0, 0, 0)
Adept = Card("Adept","You gain extra knowledge through battle gaining more experience", 0, 0, 0, 0, 0, -5)
Swift_Foot = Card("Swift Foot","You feel lighter in your body making your movements much quicker", 1, 0, 2, 0, 0, 0)
Health_Kit = Card("Health Kit","Health pack for when you need it", 0, 10, 0, 0, 0, 0)
Cursed_Weapon = Card("Cursed Weapon","You feel that your weapon becomes cursed healing you with each hit, but beware it has consequences...", -5, -5, -3, -1, 2, 20)
Charged_Return = Card("Charged Return","If your opponent has more speed than you, you deal more damage.", 0, 0, 0, 2, 0, 0)
Thresher_Claws = Card("Thresher Claws","All your attacks deal 1 more damage", 0, 0, 0, 1, 0, 0)
Aggressive_Posture = Card("Aggresive Posture","Your attacks slow down your opponent due to your high aggressiveness, not leaving breathing space", 0, 0, 5, 0, 0, 0)
Warriors_Respite = Card("Warrior's Respite","You feel your body gaining slight strength making you heal before every attack", 0, 0, 0, 0, 0, 0)



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

#Buffer mob
Buffer = Mob("Buffer", 0, 0, 0, 0, 0, "Buffer", 0)

#Area 1 
Slime = Mob("Slime", 10, 10, 1, 2, 25, "Gel", 2)

Zombie = Mob("Zombie", 8, 8, 2, 2, 25, "Rotten Flesh", 3)

Goblin = Mob("Goblin", 6, 6, 2, 2, 25, "Goblin Skull", 4)

#Area 2
Skeleton = Mob("Skeleton", 35, 35, 6, 5, 25, "Bone", 6)

Spider = Mob("Spider", 40, 40, 5, 7, 25, "Spider Eye", 5)

Wolf = Mob("Wolf", 30, 30, 8, 8, 25, "Fur", 7)

#Area 3
Golem = Mob("Golem", 100, 100, 15, 1, 25, "Magic Stone", 8)

Gargoyle = Mob("Gargoyle", 80, 80, 18, 9, 25, "Gargoyle Tooth", 9)

Ogre = Mob("Ogre", 90, 90, 20, 7, 25, "Broken Club", 12)

Snake = Mob("Snake", 5, 90 ,2 , 7, 25, "Venom", 10)

#Bosses
Gromp = Mob("Gromp", 70, 70, 10, 4, 0, "Magical Mushroom", 20)

Dragon = Mob("Dragon", 240, 240, 30, 10, 0, "Fire Breath", 50)

plural_list  = [Goblin.Drop,  Skeleton.Drop, Spider.Drop, Ogre.Drop, Gromp.Drop, Golem.Drop]

inventory_list = []

Total_Moves = []
