from src.logic.main.Tile import Ground, Wall
from src.logic.main.Item import NoItem

#TODO: make it able to read .txt or .ini files for permanent map-saves, see if there's a way to get rid of unused variable message
#contains useful methods to change or create maps
class MapHandler(object):
    def createMap(self, xSize, ySize):
        gameMap = [[Ground(NoItem()) for x in range(xSize)] for y in range(ySize)]
        return gameMap
    
    def setTile(self, gameMap, xPos, yPos, Tile):
        gameMap[xPos][yPos] = Tile
        return gameMap
    
    def createBorders(self, gameMap, xSize, ySize):
        for y in range(ySize):
            for x in range(xSize):
                if x == 0 or y == 0 or x == (xSize - 1) or y == (ySize - 1):
                    self.setTile(gameMap, x, y, Wall())