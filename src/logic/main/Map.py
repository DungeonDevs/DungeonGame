from src.logic.main.Tile import Ground, Wall
from src.logic.main.Item import Empty
from importlib import import_module
#TODO: see if there's a way to get rid of unused variable message
#contains useful methods for changeing, creating and loading maps
class MapHandler(object):
    def createMap(self, xSize, ySize):
        return [[Ground(Empty()) for x in range(xSize)] for y in range(ySize)]

    @staticmethod
    def loadMap(levelID):
        x = import_module("resources.maps.level0")
        return x.getLevel()

    def setTile(self, gameMap, xPos, yPos, Tile):
        gameMap[xPos][yPos] = Tile
        return gameMap

    def createBorders(self, gameMap, xSize, ySize):
        for y in range(ySize):
            for x in range(xSize):
                if x == 0 or y == 0 or x == (xSize - 1) or y == (ySize - 1):
                    self.setTile(gameMap, x, y, Wall())