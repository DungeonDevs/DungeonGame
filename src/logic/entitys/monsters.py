from src.logic.main.Entity import Monster, IntelligentMonster
from src.utils.astar import *
#TODO add new monsters here
class Hunter(IntelligentMonster):
    def __init__(self, xPos, yPos, orientation, attack=2, health=10, eyesight=5):
        IntelligentMonster.__init__(self, xPos, yPos, orientation, attack, health, ID = 0)
        self.eyesight = eyesight
    #this function uses pathfinding to run towards the player -> turn and direction are ignored
    def move(self, player, gameMap):
        if not self.inRange(player):
            Monster.move(self.info[2], True)
        finder = pathfinder(neighbors=self.grid_neighbors(len(gameMap), len(gameMap[0]), gameMap))
        wayLength, path = finder((self.info[0], self.info[1]), (player.info[0], player.info[1]))
        print(path)
        self.info[0], self.info[1] = path[1]

    def inRange(self, player):
        return (player.info[0] + 5 >= self.info[0] and player.info[0] -5 <= self.info[0] and player.info[1]  +5 >= self.info[1] and player.info[1]  -5 <= self.info[1])
    def grid_neighbors(self, height, width, gameMap ):
        def func( coord ):
            neighbor_list = [ ( coord[ 0 ], coord[ 1 ] + 1),
                            ( coord[ 0 ], coord[ 1 ] - 1),
                            ( coord[ 0 ] + 1, coord[ 1 ]),
                            ( coord[ 0 ] - 1, coord[ 1 ])]
            return [ c for c in neighbor_list
                    if c != coord
                    and c[0] >= 0 and c[0] < width
                    and c[1] >= 0 and c[1] < height
                    and not gameMap[c[0]][c[1]].getIsSolid()]
        return func