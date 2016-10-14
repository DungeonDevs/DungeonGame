from src.logic.main.Entity import Player
from src.logic.main.Tile import Ground

class Engine(object):
    info ={"Ground": 0, "Wall": 1}
    def __init__(self):
        pass
    def display(self, gameMap, playerXPos, playerYPos, playerOrientation):
        row = ""
        for y in range(10):
            for x in range(10):
                if x == playerXPos and y == playerYPos:
                    row += "P "
                else:
                    row += str(self.info[gameMap[x][y].getTile()])
                    if gameMap[x][y].getTile() == "Ground" and gameMap[x][y].item != 0:
                        row += str(gameMap[x][y].item)
                    else:
                        row += " "
                        
            print(row)
            row = ""
    
class InputHandler(object):
    def getInput(self):
        return input("Move:")