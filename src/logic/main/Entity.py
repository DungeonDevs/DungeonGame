import random

#superclass for mobs and player, contains shared variables and methods
class Entity(object):
    def __init__(self, xPos, yPos, orientation, attack, health):
        self.info = [0,0,0,0,0]
        self.info[0] = xPos
        self.info[1] = yPos
        self.info[2] = orientation
        self.info[3] = attack
        self.info[4] = health

    #direction = 0 is forwards - direction = 1 is backwards
    def move(self, direction):
        if direction == 0:
            if self.info[2] == 0:
                self.info[1] -= 1
            elif self.info[2] == 1:
                self.info[0] += 1
            elif self.info[2] == 2:
                self.info[1] += 1
            elif self.info[2] == 3:
                self.info[0] -= 1
        elif direction == 1:
            if self.info[2] == 0:
                self.info[1] += 1
            elif self.info[2] == 1:
                self.info[0] -= 1
            elif self.info[2] == 2:
                self.info[1] -= 1
            elif self.info[2] == 3:
                self.info[0] += 1

    #returns the position as a pair
    def getPosition(self):
        return self.info[0], self.info[1]

class Player(Entity):
    # orientation from top to left: 0,1,2,3
    def __init__(self, xPos, yPos, orientation, playerClass):
        Entity.__init__(self, xPos, yPos, orientation, playerClass.stats[1], playerClass.stats[2])
        self.info += [playerClass] #used for original stats
        self.info += [playerClass.stats[3]] #healing
        self.info += [playerClass.stats[4]] #intelligence
        self.info += [playerClass.stats[5]] #intuition
        self.info += [playerClass.stats[6]] #dexterity
        self.info += [playerClass.stats[7]] #agility
        self.info += [playerClass.stats[8]] #block

    #override in subclasses
    def heal(self):
        if (random.randint(0, self.info[5].stats[2]) - self.info[4]) > 0: #the more injured you are the more likely you will be healed
            self.info[4] += random.randint(0, self.info[5].stats[3]) #heals you for a random amount depending on the healing stat
        if (self.info[4] > self.info[5].stats[2]): #if you got healed over your max HP you are set to max HP
            self.info[4] = self.info[5].stats[2]

'''
superclass for all monsters. Can be instantiated to a monster with random movement
'''
class Monster(Entity):
    def __init__(self, xPos, yPos, orientation, attack=10, health=10, ID = 0):
        Entity.__init__(self, xPos, yPos, orientation, attack, health)
        self.ID = ID
    def move(self, direction, turn):
        if turn:
            self.info[2] = random.randint(0,4)
        Entity.move(self, direction)

'''
A class for monsters with functions need more information to work.
'''
class IntelligentMonster(Monster):
    def __init__(self, xPos, yPos, orientation, attack, health, ID = 0):
        Monster.__init__(self, xPos, yPos, orientation, attack, health, ID = ID)

    def move(self, gameMap, player, mobs, pathfinder):
        pass