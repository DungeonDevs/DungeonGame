from src.logic.main.Tile import Ground, Wall
from src.logic.main.Item import Empty
from importlib import import_module

'''
contains useful methods to handle the maps
'''
class MapHandler(object):

    '''
    creates a map filled with Ground-Tiles
    @param xSize, ySize: height/width of the map
    '''
    def createMap(self, xSize, ySize):
        return [[Ground(Empty()) for x in range(xSize)] for y in range(ySize)]
    '''
    used to load maps, maps are saved as a Python file including a getLevel method creating the gameMap
    @param levelID: ID/number of the level to load
    '''
    @staticmethod
    def loadMap(levelID):
        x = import_module("resources.maps.level" + str(levelID))
        return x.getLevel()

    '''
    used to set a specific position on the map to a specific tile
    @param gameMap: the map that is changed
    '''
    def setTile(self, gameMap, xPos, yPos, Tile):
        gameMap[xPos][yPos] = Tile
        return gameMap

    '''
    creates a border using the upper left corner and the given coordinates as corners
    @param gameMap: the map that the borders are created in
    @param xSize, ySize: the coordinates of the bottom right corner
    '''
    def createBorders(self, gameMap, xSize, ySize):
        for y in range(ySize):
            for x in range(xSize):
                if x == 0 or y == 0 or x == (xSize - 1) or y == (ySize - 1):
                    self.setTile(gameMap, x, y, Wall())