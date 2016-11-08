class playerClass():
    def __init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block):
        self.stats = [0,0,0,0,0,0,0,0,0]
        self.stats[0] = ID
        self.stats[1] = attack
        self.stats[2] = health
        self.stats[3] = healing
        self.stats[4] = intelligence
        self.stats[5] = intuition
        self.stats[6] = dexterity
        self.stats[7] = agility
        self.stats[8] = block

class Knight(playerClass):
    def __init__(self, ID = 0, attack = 10, health = 30, healing = 3, intelligence = 1, intuition = 5, dexterity = 1, agility = 2, block = 10):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)
        
class Healer(playerClass):
    def __init__(self, ID = 1, attack = 5, health = 40, healing = 10, intelligence = 10, intuition = 2, dexterity = 3, agility = 5, block = 2):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)
        
class Adventurer(playerClass):
    def __init__(self, ID = 2, attack = 7, health = 20, healing = 5, intelligence = 7, intuition = 8, dexterity = 6, agility = 10, block = 1):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)
        
class Thief(playerClass):
    def __init__(self, ID = 3, attack = 5, health = 10, healing = 1, intelligence = 25, intuition = 10, dexterity = 20, agility = 30, block = 0):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)