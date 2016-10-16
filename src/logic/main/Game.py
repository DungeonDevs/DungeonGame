from src.logic.main.Map import MapHandler
from src.logic.main.Entity import Player, Monster, IntelligentMonster

from src.logic.main.Engine import Engine, InputHandler
from src.logic.main.Item import Empty, LevelEnd, Interactable, Item
#import for testing only
from src.logic.main.Items import Leather, Sword
from src.logic.entitys.monsters import Hunter
#from src.logic.main.Tile import Wall
#from src.logic.main.Item import SolidItem
import time
#TODO: clean this up, remove test-code
#main class, contains main-loop
class Game(object):

    engine = Engine()
    inputHandler = InputHandler()
    mapHandler = MapHandler()
    gameMap = mapHandler.createMap(10, 10)
    gameMap[8][8].setGameObject(Leather())
    #gameMap[1][2].setGameObject(LevelEnd())
    levelID = 0 # stores which level is played right now
    #gameMap[2][2] = Wall()
    #gameMap[2][4].setItem(SolidItem())
    player = Player(1,1,1,10,30, None)
    mobs = [Monster(5,5,0,5,21),Monster(5,5,0,5,21),Monster(5,5,0,5,21), Hunter(5,5,0,2,10,100)]
    #mobs += [Monster(5,5,0,5,21)]
    #mobs += [Monster(4,4,0,5,21)]
    #mobs += [Monster(2,6,0,5,21)]
    running = True
    gameWon = None
    '''
    @param: hero - the hero to use
    @param: callback - a callback that s called when the game ends. True is handed over if the player won
    '''
    def __init__(self, hero = None, callback = None):
        # if hero is presented the player is set to hero
        if(not (hero is None)):
            player = hero
        self.mapHandler.createBorders(self.gameMap, 10,10)
        self.deltaTime = time.time()
        while self.running:
            self.tick()
            if(self.running is False):
                break
        if(callback):
            callback(gameWon)

    def tick(self):
        self.display()
        print("deltaTime: " + str(time.time() - self.deltaTime))
        self.playerMove()
        self.deltaTime  = time.time()
        self.mobMove()
        self.fight()
        self.gameObjectAction()
        self.checkHealth()

    def display(self):
        self.engine.display(self.gameMap, self.player.info, self.mobs)

    def playerMove(self):
        inputKey = self.inputHandler.getInput()
        if inputKey == "w":
            self.player.move(0)
            if self.gameMap[self.player.info[0]][self.player.info[1]].getIsSolid() or self.gameMap[self.player.info[0]][self.player.info[1]].gameObject.isSolid:
                self.player.move(1)
        elif inputKey == "a":
            self.player.info[2] -= 1
            if self.player.info[2] < 0:
                self.player.info[2] = 3
        elif inputKey == "d":
            self.player.info[2] += 1
            if self.player.info[2] > 3:
                self.player.info[2] = 0
        elif inputKey == "s":
            self.player.move(1)
            if self.gameMap[self.player.info[0]][self.player.info[1]].getIsSolid() or self.gameMap[self.player.info[0]][self.player.info[1]].gameObject.isSolid:
                self.player.move(0)
        elif inputKey == "stop":
            self.running = False

    def mobMove(self):
        for a in range(len(self.mobs)):
            #intelliget monsters behave another way

            if(isinstance(self.mobs[a], IntelligentMonster)):
                print(self.mobs[a].info)
                self.mobs[a].move(self.player,self.gameMap)
                continue
            self.mobs[a].move(0, True)
            if self.gameMap[self.mobs[a].info[0]][self.mobs[a].info[1]].getIsSolid() or self.gameMap[self.mobs[a].info[0]][self.mobs[a].info[1]].gameObject.isSolid:
                self.mobs[a].move(1, False)

    def fight(self):
        dead = []
        for a in range(len(self.mobs)):
            if self.mobs[a].info[0] == self.player.info[0] and self.mobs[a].info[1] == self.player.info[1]:
                self.player.info[4] -= (self.mobs[a].info[4] / self.player.info[3])*self.mobs[a].info[3]
                if (not self.player.info[4] <= 0):
                    #TODO: heal the player self.player.heal() (already implemented)
                    dead += [a]

        for a in range(len(dead)):
            self.mobs.pop(dead[a])

    def gameObjectAction(self):
        gameObject = self.gameMap[self.player.info[0]][self.player.info[1]].gameObject

        if isinstance(gameObject, Empty):
            return

        #use the stats of the item to buff the player
        if isinstance(gameObject, Item):
            self.player.info[3] += gameObject.attackUp
            self.player.info[4] += gameObject.healthUp

        # handing over a callback so different LevelEnd-items can behave in different ways
        if isinstance(gameObject, LevelEnd):
            gameObject.trigger(self.loadNextLevel)

        # handing over a few important objects, so different InteractableObejcts can behave in interesting different ways
        if isinstance(gameObject, Interactable):
            gameObject.interact(self.player, self.gameMap, self.mobs)

        self.gameMap[self.player.info[0]][self.player.info[1]].setGameObject(Empty())

    def checkHealth(self):
        if self.player.info[4] <= 0:
                    self.gameWon = False
                    print("You lost!")
                    self.running = False

    def loadNextLevel(self, levelToLoad = None, EndGame = False):
        if(EndGame):
            self.gameWon = True
            return
        if(not levelToLoad is None): # if a levelToLoad is hand over load this level
             self.levelID = levelToLoad
        else: # else load the level with the next id
            self.levelID = self.levelID + 1

        self.gameMap, self.mobs, self.player.info[0], self.player.info[1] = MapHandler.loadMap(levelID)
        self.mapHandler.createBorders(self.gameMap, len(self.gameMap),len(self.gameMap[0]))