from src.logic.main.Tile import Ground, Wall
from src.logic.main.Item import Empty
import json
#TODO: make use it´s ability to read .json files for permanent map-saves, see if there's a way to get rid of unused variable message
#contains useful methods to change or create maps
class MapHandler(object):
    def createMap(self, xSize, ySize):
        return [[Ground(Empty()) for x in range(xSize)] for y in range(ySize)]

    @staticmethod
    def loadMap(self, levelID):
        data = json.load(open(str(levelID) + '.json'))
        gameMap = data["map"] # a gameMap
        mobs = data ["mobs"] # a list of mob infos
        playerPosition = data["playerPosition"] #for example [12,7]
        return gameMap, mobs, playerPosition[0], playerPosition[1]

    @staticmethod
    def saveMap(levelID, gameMap, playerPosition, mobs, levelType=0):
        levelFile = open(str(levelID) + '.json')
        json.dump({"levelID": levelID,"gameMap":gameMap, "playerPosition": playerPosition, "mobs": mobs, "levelType": levelType}, levelFile)

    def setTile(self, gameMap, xPos, yPos, Tile):
        gameMap[xPos][yPos] = Tile
        return gameMap

    def createBorders(self, gameMap, xSize, ySize):
        for y in range(ySize):
            for x in range(xSize):
                if x == 0 or y == 0 or x == (xSize - 1) or y == (ySize - 1):
                    self.setTile(gameMap, x, y, Wall())