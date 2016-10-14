from src.logic.main.Tile import Ground

class MapHandler(object):
    def createMap(self, xSize, ySize):
        gameMap = [[Ground(0) for x in range(xSize)] for y in range(ySize)]
        return gameMap
    
    def setTile(self, gameMap, xPos, yPos, Tile):
        gameMap[xPos][yPos] = Tile
        return gameMap