from src.logic.main.Entity import Monster, IntelligentMonster
from src.utils.astar import *
#TODO add new monsters here
class Hunter(IntelligentMonster):
    def __init__(self, xPos, yPos, orientation, attack=2, health=10, eyesight=5):
        IntelligentMonster.__init__(self, xPos, yPos, orientation, attack, health, ID = 0)
        self.eyesight = eyesight

    #this function uses pathfinding to run towards the player -> turn and direction are ignored
    def move(self, gameMap, player, mobs, pathfinder):
        if not self.inRange(player): # behave like  a normal monster if you do not see the player
            Monster.move(self, self.info[2], True)
        elif player.getPosition() == self.getPosition(): #if you hunted the player down do not move
            pass
        else: #use pathfinding to move towards the player
            pathLength, path = pathfinder((self.info[0], self.info[1]), (player.info[0], player.info[1]))
            self.info[0], self.info[1] = path[1]

    '''
    checks whether the target entity is in range.
    '''
    def inRange(self, target):
        return (target.info[0] + self.eyesight >= self.info[0] and
         target.info[0] -self.eyesight <= self.info[0] and
          target.info[1]  +self.eyesight >= self.info[1] and
           target.info[1]  -self.eyesight <= self.info[1])