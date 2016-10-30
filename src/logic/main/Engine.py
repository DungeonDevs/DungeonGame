
#everything is temporary and is in no way optimized
class DebugEngine(object):
    info ={"Ground": 0, "Wall": 1}
    def __init__(self):
        pass
    def display(self, gameMap, playerInfo, mobs):
        field = ["" for x in range(len(gameMap[0]))]
        row = ""
        for y in range(len(gameMap[0])):
            for x in range(len(gameMap)):
                row += str(self.info[gameMap[x][y].getTile()])
                if gameMap[x][y].gameObject.ID != 0:
                    row += str(gameMap[x][y].gameObject.ID)
                else:
                    row += " "
            field[y] = row
            row = ""

        replace = field[playerInfo[1]]
        replace = replace[0: 2 * playerInfo[0]] + "P " + replace[2 * (playerInfo[0] + 1): -1] + " "
        field[playerInfo[1]] = replace

        for a in range(len(mobs)):
            replace = field[mobs[a].info[1]]
            replace = replace[0: 2 * mobs[a].info[0]] + "M " + replace[2 * (mobs[a].info[0] + 1): -1] + " "
            field[mobs[a].info[1]] = replace

        for y in range(len(gameMap[0])):
            print(field[y])
        print("Health: " + str(playerInfo[4])+ "/" + str(playerInfo[5].stats[2]) + " Attack: " + str(playerInfo[3]) + " Healing: " + str(playerInfo[5].stats[3]))
        print(playerInfo[0:5] + playerInfo[6:12])

from engine.Engine import Engine, Direction
from engine.classes.RenderObject import RenderObject
from engine.classes.LoadedObject import LoadedObject
from src.logic.main.Item import Empty
import pygame
'''
An Interface to display the world with PyEngine.
@param: debug - when set to True the legacy textengine is used to display debuginformation.
TODO: Add items and mobs to display
'''
class EngineInterface(object):
    def __init__(self, debug = False):
        self.ground = RenderObject.createOneColorCube((150/255, 75/255, 0))
        self.wall = RenderObject.createOneColorCube((100/255, 100/255, 0))
        self.item = LoadedObject("engine.resources.block", 16)
        self.item.setGroundNecessary(True)
        self.playermodel = LoadedObject("resources.heroes.charakter1", 32)
        #self.mob = RenderObject.createOneColorCube((255/255, 0, 0))
        self.engine = Engine((600, 400))
        self.engine.setGround(self.ground)
        self.engine.startUp()
        if debug:
            self.debug = True
            self.debugEngine = DebugEngine()

    def display(self, gameMap, playerInfo, mobs):
        if self.debug:
            self.debugEngine.display(gameMap, playerInfo, mobs)
        convertedMap = gameMap.copy()
        convertedMap = [[None for c in range(len(gameMap[0]))] for i in range(len(gameMap))]
        for y in range(len(gameMap[0])):
            for x in range(len(gameMap)):
                if( gameMap[x][y].getIsSolid()):
                    convertedMap[x][y] = self.wall
                else:
                    self.playermodel
                    if not isinstance(gameMap[x][y].gameObject,Empty):
                        convertedMap[x][y] = self.item
        #for mob in mobs:
        #    convertedMap[mob.info[0]][mob.info[1]] = self.mob
        convertedMap[playerInfo[1]][playerInfo[0]] = self.playermodel
        self.engine.setMap(convertedMap)
        self.engine.setPlayerPosInfo(playerInfo[0], playerInfo[1], playerInfo[2])
        self.engine.render()
class InputHandler(object):
    def getInput(self):
        return input("Move:")