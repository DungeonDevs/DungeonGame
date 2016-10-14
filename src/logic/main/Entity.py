import random
#superclass for mobs and player, contains shared variables and methods
class Entity(object):
    def __init__(self, xPos, yPos, orientation, attack, health):
        self.info = [0,0,0,0,0,0]
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
            if self.info[2] == 1:
                self.info[0] += 1
            if self.info[2] == 2:
                self.info[1] += 1
            if self.info[2] == 3:
                self.info[0] -= 1
        elif direction == 1:
            if self.info[2] == 0:
                self.info[1] += 1
            if self.info[2] == 1:
                self.info[0] -= 1
            if self.info[2] == 2:
                self.info[1] -= 1
            if self.info[2] == 3:
                self.info[0] += 1

#TODO: implement different playerClasses        
class Player(Entity):
    # orientation from top to left: 0,1,2,3
    def __init__(self, xPos, yPos, orientation, attack, health, playerClass):
        Entity.__init__(self, xPos, yPos, orientation, attack, health)
        self.info[5] = playerClass

#TODO: make their movement more interesting/intelligent/less random
#basic opponent     
class Monster(Entity):
    def __init__(self, xPos, yPos, orientation, attack, health):
        Entity.__init__(self, xPos, yPos, orientation, attack, health)
    
    def move(self, direction, turn):
        if turn:
            self.info[2] = random.randint(0,4)
        Entity.move(self, direction)