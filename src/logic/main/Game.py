from src.logic.main.Map import MapHandler
from src.logic.main.Entity import Player, Monster, IntelligentMonster
import src.utils.astar as astar
import random
from src.logic.main.Engine import Engine, InputHandler
from src.logic.main.Item import Empty, LevelEnd, Interactable, Item

#imports for testing only
from src.logic.objects.GameObjects import Leather, Sword
from src.logic.objects.Monsters import Hunter
from src.logic.main.PlayerClass import Knight, Healer, Adventurer, Thief

'''
main class, contains the main loop and the corresponding methods
'''
class Game(object):

    #creates the needed engine, inputHandler and mapHandler
    engine = Engine()
    inputHandler = InputHandler()
    mapHandler = MapHandler()

    levelID = 0 # stores which level is played right now
    levels = 2 #amount of levels there are
    player = Player(1,1,1,Knight())

    #function to generate paths between tiles
    pathfinding = None
    #while True the main loop is active
    running = True
    gameWon = None
    '''
    @param: hero - the hero to use
    @param: callback - a callback that s called when the game ends. True is handed over if the player won
    '''
    def __init__(self, hero, callback = None):
        # if hero is presented the player is set to hero
        if(not (hero is None)):
            self.player = Player(1,1,1,hero)
        self.loadLevel(levelToLoad = 0) # load first level
        #main loop as long as the game is running
        while self.running:
            self.tick()
        #when the game has ended
        if(callback):
            callback(self.gameWon)

    #is run every tick of the game
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
    #tick 1 - blocking input method
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
        self.player.heal()

    #tick 2
    def mobMove(self):
        for a in range(len(self.mobs)):
            #intelligent monsters behave another way
            if isinstance(self.mobs[a], IntelligentMonster):
                #print(self.mobs[a].info)
                self.mobs[a].move(self.gameMap, self.player, self.mobs, self.pathfinding)
                continue
            self.mobs[a].move(0, True)
            if self.gameMap[self.mobs[a].info[0]][self.mobs[a].info[1]].getIsSolid() or self.gameMap[self.mobs[a].info[0]][self.mobs[a].info[1]].gameObject.isSolid or self.player.info[7] > random.randint(0, 100): #basic monsters randomly don't attack you if you are intelligent enough
                self.mobs[a].move(1, False)
    #tick 3
    def fight(self):
        dead = []
        for a in range(len(self.mobs)):

            #if player and mob are on the same coordinates
            if self.mobs[a].info[0] == self.player.info[0] and self.mobs[a].info[1] == self.player.info[1]:
                #randomly no damage taken at all, depends on agility, dexterity and intuition
                if (self.player.info[9] + self.player.info[10] + self.player.info[8]) < random.randint(0, 150):
                    #damage taken depends on players attack and block (and monsters attack and health)
                    self.player.info[4] -= ((self.mobs[a].info[4] / self.player.info[3])*self.mobs[a].info[3]) / (100/self.player.info[11])
                #if player isn't dead, the mob is
                if (not self.player.info[4] <= 0):
                    dead += [a]

        #all dead mobs are removed from the list
        a = len(dead)
        while a > 0:
            self.mobs.pop(dead[a - 1])
            a -= 1

    #tick 4
    def gameObjectAction(self):
        gameObject = self.gameMap[self.player.info[0]][self.player.info[1]].gameObject

        if isinstance(gameObject, Empty):
            return
        #use the stats of the item to buff the player
        if isinstance(gameObject, Item):
            self.player.info[3] += gameObject.attackUp
            self.player.info[4] += gameObject.healthUp
            self.player.info[5].stats[2] += gameObject.healthUp
            self.player.info[6] += gameObject.healingUp
            self.player.info[7] += gameObject.intelligenceUp
            self.player.info[8] += gameObject.intuitionUp
            self.player.info[9] += gameObject.dexterityUp
            self.player.info[10] += gameObject.agilityUp
            self.player.info[11] += gameObject.blockUp

        # handing over a callback so different LevelEnd-items can behave in different ways
        if isinstance(gameObject, LevelEnd):
            print("Level done!")
            self.levelID += 1
            if self.levelID > self.levels:
                self.gameWon = True
                self.running = False
            else:
                try:
                    self.loadLevel(levelToLoad=self.levelID)
                except Exception as e:
                    print(e)
                    self.gameWon = True
                    self.running = False

        # handing over a few important objects, so different InteractableObejcts can behave in interesting different ways
        if isinstance(gameObject, Interactable):
            gameObject.interact(self.player, self.gameMap, self.mobs)

        self.gameMap[self.player.info[0]][self.player.info[1]].setGameObject(Empty())

    #tick 5 last
    def checkHealth(self):
        if self.player.info[4] <= 0:
                    self.gameWon = False
                    self.running = False
        '''
        elif(len(self.mobs) == 0):
            print("Level done!")
            self.levelID += 1
            self.loadLevel(levelToLoad=self.levelID)
        '''

    #loads the current level
    def loadLevel(self, levelToLoad = None):
        #if(EndGame):
        #    self.gameWon = True
        #    return
        #if(not levelToLoad is None): # if a levelToLoad is hand over load this level
        self.levelID = levelToLoad
        #else: # else load the level with the next id
        #    self.levelID = self.levelID + 1

        self.gameMap, self.mobs, self.player.info[0], self.player.info[1] = MapHandler.loadMap(self.levelID)
        self.mapHandler.createBorders(self.gameMap, len(self.gameMap),len(self.gameMap[0]))
        self.pathfinding = astar.pathfinder(astar.gamemapNeighbors(self.gameMap))