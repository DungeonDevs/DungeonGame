class Entity(object):
    def __init__(self, xPos, yPos, orientation, attack, health):
        self.xPos = xPos
        self.yPos = yPos
        self.orientation = orientation
        self.attack = attack
        self.health = health
        
class Player(Entity):
    # orientation from top to left: 0,1,2,3
    def __init__(self, xPos, yPos, orientation, attack, health, playerClass):
        Entity.__init__(self, xPos, yPos, orientation, attack, health)
        self.playerClass = playerClass
    
    def move(self):
        if self.orientation == 0:
            self.yPos -= 1
        if self.orientation == 1:
            self.xPos += 1
        if self.orientation == 2:
            self.yPos += 1
        if self.orientation == 3:
            self.xPos -= 1