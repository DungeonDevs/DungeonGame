from src.logic.main.Map import MapHandler
from src.logic.main.Entity import Player, Monster, IntelligentMonster
import src.utils.astar as astar
from src.logic.main.Engine import Engine, InputHandler
from src.logic.main.Item import Empty, LevelEnd, Interactable, Item
#imports for testing only
from src.logic.objects.GameObjects import Leather, Sword
from src.logic.objects.Monsters import Hunter
#TODO: clean this up, remove test-code
#main class, contains main-loop
class Game(object):

    engine = Engine()
    inputHandler = InputHandler()
    mapHandler = MapHandler()

    #gameMap = mapHandler.createMap(10, 10)
    #gameMap[8][8].setGameObject(Leather())
    levelID = 0 # stores which level is played right now
    player = Player(1,1,1,10,30, None)
    #mobs = [Monster(5,5,0,5,21),Monster(5,5,0,5,21),Monster(5,5,0,5,21), Hunter(5,5,0,2,10,100)]
    pathfinding = None #function to generate paths between tiles
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
        self.loadLevel(levelToLoad = 0) # load first level
        while self.running:
            self.tick()
            if(self.running is False):
                break
        if(callback):
            callback(gameWon)

    #called in the main loop
    def tick(self):
        self.display()
        self.playerMove()
        self.mobMove()
        self.fight()
        self.gameObjectAction()
        self.checkHealth()
    #tick 0
    def display(self):
        self.engine.display(self.gameMap, self.player.info, self.mobs)
    #tick 1 - blocking input Methode
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

    #tick 2
    def mobMove(self):
        for a in range(len(self.mobs)):
            #intelligent monsters behave another way
            if isinstance(self.mobs[a], IntelligentMonster):
                print(self.mobs[a].info)
                self.mobs[a].move(self.gameMap, self.player, self.mobs, self.pathfinding)
                continue
            self.mobs[a].move(0, True)
            if self.gameMap[self.mobs[a].info[0]][self.mobs[a].info[1]].getIsSolid() or self.gameMap[self.mobs[a].info[0]][self.mobs[a].info[1]].gameObject.isSolid:
                self.mobs[a].move(1, False)
    #tick 3
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
    #tick 4
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

    #tick 5 last
    def checkHealth(self):
        if self.player.info[4] <= 0:
                    self.gameWon = False
                    print("You lost!")
                    self.running = False


    def loadLevel(self, levelToLoad = None, EndGame = False):
        if(EndGame):
            self.gameWon = True
            return
        if(not levelToLoad is None): # if a levelToLoad is hand over load this level
             self.levelID = levelToLoad
        else: # else load the level with the next id
            self.levelID = self.levelID + 1

        self.gameMap, self.mobs, self.player.info[0], self.player.info[1] = MapHandler.loadMap(self.levelID)
        self.mapHandler.createBorders(self.gameMap, len(self.gameMap),len(self.gameMap[0]))
        self.pathfinding = astar.pathfinder(neighbors=astar.grid_neighbors_custom(len(self.gameMap), len(self.gameMap[0]), self.gameMap), cost=astar.custom_costs(self.gameMap))