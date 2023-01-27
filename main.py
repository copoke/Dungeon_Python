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
class Move:
    def __init__(self, Name, Description, Cost, HP, Speed, DMG, Lifesteal, Level):
        self.Name = Name
        self.Description = Description
        self.Cost = Cost
        self.HP = HP
        self.Speed = Speed
        self.DMG = DMG
        self.Lifesteal = Lifesteal
        self.Level = Level
#Player classes
Bruiser = Player("Bruiser", 25, 25, 3, 3, 0, 100, 1, 0, 10, 10, 0)

Tank = Player("Tank", 30, 30, 2, 1, 0, 100, 1, 0, 5, 5, 0)

Assasin = Player("Assasin", 20, 20, 4, 4, 0, 100, 1, 0, 20, 20, 0)

#Player Cards
Lethal_Precision = Card("Lethal Precision", "You gain more precision in your attacks, making your hits land with greater strength", 1, 0, 0, 1, 0, 0)
Brutal_Momentum = Card("Brutal Momentum", "With every swing you keep your momentum, giving you more speed in your hits", 0, 0, 2, 0, 0, 0)
Adept = Card("Adept","You gain extra knowledge through battle gaining more experience", 0, 0, 0, 0, 0, -5)
Swift_Foot = Card("Swift Foot","You feel lighter in your body making your movements much quicker", 1, 0, 2, 0, 0, 0)
Health_Kit = Card("Health Kit","Health pack for when you need it", 0, 10, 0, 0, 0, 0)
Cursed_Weapon = Card("Cursed Weapon","You feel that your weapon becomes cursed healing you with each hit, but beware it has consequences...", -5, -5, -3, -1, 2, 20)
Charged_Return = Card("Charged Return","Gain more damage in exchange for speed", 0, 0, 0, -2, 2, 0)
Thresher_Claws = Card("Thresher Claws","All your attacks deal 1 more damage", 0, 0, 0, 1, 0, 0)
Aggressive_Posture = Card("Aggresive Posture","Your attacks slow down your opponent due to your high aggressiveness, not leaving breathing space", 0, 0, 5, 0, 0, 0)
Warriors_Respite = Card("Warrior's Respite","You feel your body gaining slight strength making you heal with every attack", 0, 0, 0, 0, 2, 0)
Angled_Fighter = Card("Angled Fighter","Your sword hits at better angles hitting different points dealing more damage in exchange for slower attacks with more accuracy",0, 0, -3, 2, 0, 0)

card_list = [Lethal_Precision,  Brutal_Momentum, Adept,  Swift_Foot, Health_Kit, Cursed_Weapon, Charged_Return, Thresher_Claws, Aggressive_Posture, Warriors_Respite]

#Player Moves

Thrust = Move("Thrust","Slash your sword through your opponent", -10, 0, -5, 5, 1, 2)
Rapid_Slashes = Move("Rapid Slashes","Hit your opponent with a set of quick slashes", -5, 0, 5, 2, 0, 1)
Meteor_Slash = Move("Meteor Slash", "A slash at the speed and strength as a meteor", -5, 0, 0, 0, 0, 3)
Supernova = Move("Supernova", "A last resort for whenever you need it the most, has major drawbacks", -20, -10, -5, 100, 0, 8)
Fireburst = Move("Fireburst", "A magic spell scorching the enemy for damage", -8, 0, 2, 12, 0, 4)
Heavy_Attack = Move("Heavy Slash", "A slow attack that deals bonus damage", -5, 0, -10, 10, 0, 1)
Quick_Attack = Move("Quick Attack", "A quick attack making the user gain immense amount of speed at the cost of some damage", -4, 0, 15, -2, 0, 1)
Blood_Steal = Move("Blood Steal", "Steal the enemys health healing you and dealing damage to the enemy", -10, 10, 0, 20, 0, 6)
Decimating_Blow= Move("Decimating Blow", "A skull crushing blow, dealing heavy damage", -8, 0, 0, 5, 0, 2)

current_weapon = ""

move_list = [Thrust, Rapid_Slashes, Meteor_Slash, Supernova, Fireburst, Heavy_Attack, Quick_Attack, Blood_Steal, Decimating_Blow]
character_move_list = []

#Area 1 
Slime = Mob("Slime", 10, 10, 1, 2, 25, "Gel", 2)

Zombie = Mob("Zombie", 8, 8, 2, 2, 25, "Rotten Flesh", 3)

Goblin = Mob("Goblin", 6, 6, 2, 2, 25, "Goblin Skull", 4)

#Area 2
Skeleton = Mob("Skeleton", 35, 35, 6, 5, 40, "Bone", 6)

Spider = Mob("Spider", 40, 40, 5, 7, 40, "Spider Eye", 5)

Wolf = Mob("Wolf", 30, 30, 8, 8, 40, "Fur", 7)

#Area 3
Golem = Mob("Golem", 100, 100, 15, 1, 60, "Magic Stone", 8)

Gargoyle = Mob("Gargoyle", 80, 80, 18, 9, 60, "Gargoyle Tooth", 9)

Ogre = Mob("Ogre", 90, 90, 20, 7, 60, "Broken Club", 12)

Snake = Mob("Snake", 5, 90 ,2 , 7, 25, "Venom", 10)

#Bosses
Gromp = Mob("Gromp", 30, 30, 6, 4, 0, "Magical Mushroom", 20)

Dragon = Mob("Dragon", 100, 100, 10, 10, 0, "Fire Breath", 50)

plural_list  = [Goblin.Drop,  Skeleton.Drop, Spider.Drop, Ogre.Drop, Gromp.Drop, Golem.Drop]

inventory_list = []

character_move_list = []
