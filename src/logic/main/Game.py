from src.logic.main.Map import MapHandler
from src.logic.main.Entity import Player, Monster

from src.logic.main.Engine import Engine, InputHandler
from src.logic.main.Item import NoItem, Sword, LevelEnd, Interactable
#from src.logic.main.Tile import Wall
#from src.logic.main.Item import SolidItem

#TODO: clean this up, remove test-code
#main class, contains main-loop
class Game(object):

    engine = Engine()
    inputHandler = InputHandler()
    mapHandler = MapHandler()
    gameMap = mapHandler.createMap(10, 10)
    gameMap[8][8].setItem(Sword())
    gameMap[1][2].setItem(LevelEnd())
    levelID = 0 # stores which level is played right now
    #gameMap[2][2] = Wall()
    #gameMap[2][4].setItem(SolidItem())
    player = Player(1,1,1,10,30, None)
    mobs = [Monster(5,5,0,5,21),Monster(5,5,0,5,21),Monster(5,5,0,5,21)]
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
        while self.running:
            self.tick()
            if(self.running is False):
                break
        if(callback):
            callback(gameWon)

    def tick(self):
        self.display()
        self.playerMove()
        self.mobMove()
        self.fight()
        self.itemAction()
        self.checkHealth()

    def display(self):
        self.engine.display(self.gameMap, self.player.info, self.mobs)

    def playerMove(self):
        inputKey = self.inputHandler.getInput()
        if inputKey == "w":
            self.player.move(0)
            if self.gameMap[self.player.info[0]][self.player.info[1]].getIsSolid() or self.gameMap[self.player.info[0]][self.player.info[1]].item.isSolid:
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
            if self.gameMap[self.player.info[0]][self.player.info[1]].getIsSolid() or self.gameMap[self.player.info[0]][self.player.info[1]].item.isSolid:
                self.player.move(0)
        elif inputKey == "stop":
            self.running = False

    def mobMove(self):
        for a in range(len(self.mobs)):
            self.mobs[a].move(0, True)
            if self.gameMap[self.mobs[a].info[0]][self.mobs[a].info[1]].getIsSolid() or self.gameMap[self.mobs[a].info[0]][self.mobs[a].info[1]].item.isSolid:
                self.mobs[a].move(1, False)

    def fight(self):
        dead = []
        for a in range(len(self.mobs)):
            if self.mobs[a].info[0] == self.player.info[0] and self.mobs[a].info[1] == self.player.info[1]:
                self.player.info[4] -= (self.mobs[a].info[4] / self.player.info[3])*self.mobs[a].info[3]
                if (not self.player.info[4] <= 0):
                    #TODO: heal the player self.player.heal()
                    dead += [a]

        for a in range(len(dead)):
            self.mobs.pop(dead[a])

    def itemAction(self):
        item = self.gameMap[self.player.info[0]][self.player.info[1]].item

        if item != NoItem():
            self.player.info[3] += item.attackUp
            self.player.info[4] += item.healthUp
            self.gameMap[self.player.info[0]][self.player.info[1]].setItem(NoItem())

        if isinstance(item, LevelEnd):
            item.trigger(self.loadNextLevel) # handing over a callback so diverent LevelEnd-items can behave in different ways

        if isinstance(item, Interactable):
            item.interact(self.player, self.gameMap, self.mobs)

    def checkHealth(self):
        if self.player.info[4] <= 0:
                    self.gameWon = False
                    print("You lost!")
                    self.running = False

    def loadNextLevel(self, levelToLoad = None, EndGame = False):
        if(EndGame):
            self.gameWon = True

        if(not levelToLoad is None): # if a levelToLoad is hand over load this level
             self.levelID = levelToLoad
        else: # else load the level with the next id
            self.levelID = self.levelID + 1

        self.gameMap, self.mobs, self.player.info[0], self.player.info[1] = MapHandler.loadMap(levelID)
        self.mapHandler.createBorders(self.gameMap, len(self.gameMap),len(self.gameMap[0]))