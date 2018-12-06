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

class Dragon(playerClass):
    def __init__(self, ID = 4, attack = 30, health = 50, healing = 0, intelligence = 0, intuition = 0, dexterity = 0, agility = 0, block = 0):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)

class Tank(playerClass):
    def __init__(self, ID = 5, attack = 5, health = 50, healing = 0, intelligence = 0, intuition = 0, dexterity = 0, agility = 0, block = 15):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)

class Nerd(playerClass):
    def __init__(self, ID = 6, attack = 1, health = 10, healing = 1, intelligence = 50, intuition = 50, dexterity = 0, agility = 0, block = 0):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)

class AngryGrandmother(playerClass):
    def __init__(self, ID = 7, attack = 20, health = 15, healing = 3, intelligence = 35, intuition = 0, dexterity = 0, agility = 0, block = 0):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)

class AppleFanboy(playerClass):
    def __init__(self, ID = 8, attack = 1, health = 1, healing = 0, intelligence = 0, intuition = 0, dexterity = 0, agility = 0, block = 0):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)

class SamsungFanboy(playerClass):
    def __init__(self, ID = 9, attack = 100, health = 100, healing = 100, intelligence = 100, intuition = 100, dexterity = 100, agility = 100, block = 100):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)

class Error404(playerClass):
    def __init__(self, ID = 10, attack = 1, health = 100, healing = 5, intelligence = 0, intuition = 0, dexterity = 30, agility = 0, block = 0):
        playerClass.__init__(self, ID, attack, health, healing, intelligence, intuition, dexterity, agility, block)