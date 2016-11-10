from src.logic.main.Map import MapHandler
from src.logic.main.Entity import Player, Monster, IntelligentMonster
import src.utils.astar as astar
import random
from src.logic.main.Engine import EngineInterface as Engine, InputHandler
from src.logic.main.Item import Empty, LevelEnd, Interactable, Item, Spawner
import pygame
#imports for testing only
from src.logic.objects.Monsters import Hunter
from src.logic.main.PlayerClass import Knight, Healer, Adventurer, Thief
import time

'''
main class, contains the main loop and the corresponding methods
'''
class Game(object):

    #creates the needed #inputHandler and mapHandler
    #inputHandler = InputHandler()
    mapHandler = MapHandler()

    levelID = 0 # stores which level is played right now
    levels = 4 #amount of levels there are
    player = Player(1,1,1,Knight())

    #function to generate paths between tiles
    pathfinding = None
    #while True the main loop is active
    running = True
    gameWon = None
    '''
    @param: hero - the hero to use
    '''
    def __init__(self, hero):
        #call the engine setup in gamesetup
        self.engine = Engine(hero,debug = False)
        #block events to make the thing run faster
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
        pygame.event.set_blocked(pygame.JOYAXISMOTION)
        pygame.event.set_blocked(pygame.JOYBALLMOTION)
        pygame.event.set_blocked(pygame.KEYUP)
        # if hero is presented the player is set to hero
        if(not (hero is None)):
            self.player = Player(1,1,1,hero)
        self.loadLevel(levelToLoad = 0) # load first level
        #main loop as long as the game is running
        self.playerMoved = False
        self.displayFirst = True
        while self.running:
            self.tick()
        if(self.gameWon):
            print("You WON!")
        else:
            print("GAMEOVER!")

    #is run every tick of the game
    def tick(self):
        pygame.time.wait(1000)
        if(self.displayFirst):
            self.display()
            self.displayFirst = False
        else:
            self.playerMove()
        if(self.playerMoved and self.displayFirst):
            return
        if(self.playerMoved): #only run if the player moved
            self.mobMove()
            self.fight()
            self.gameObjectAction()
            self.checkHealth()
            self.playerMoved = False
            self.displayFirst = True
            pygame.event.clear()
    #tick 0
    def display(self):
        self.engine.display(self.gameMap, self.player.info, self.mobs)
    #tick 1 - nonblocking input method
    def playerMove(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                self.gameWon = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                #print("input: ", event.key)
                if event.key == pygame.K_w:
                    self.player.move(0)
                    if self.gameMap[self.player.info[0]][self.player.info[1]].getIsSolid() or self.gameMap[self.player.info[0]][self.player.info[1]].gameObject.isSolid:
                        self.player.move(1)
                elif event.key == pygame.K_a:
                    self.player.info[2] -= 1
                    if self.player.info[2] < 0:
                        self.player.info[2] = 3
                elif event.key == pygame.K_d:
                    self.player.info[2] += 1
                    if self.player.info[2] > 3:
                        self.player.info[2] = 0
                elif event.key == pygame.K_s:
                    self.player.move(1)
                    if self.gameMap[self.player.info[0]][self.player.info[1]].getIsSolid() or self.gameMap[self.player.info[0]][self.player.info[1]].gameObject.isSolid:
                        self.player.move(0)
                else:
                    return
                self.player.heal()
                self.playerMoved = True
                #self.displayFirst = True
        '''Old Way of getting Input

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
        '''
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
                    #self.player.info[4] -= ((self.mobs[a].info[4] / self.player.info[3])*self.mobs[a].info[3]) / (100/self.player.info[11])
                    damageTaken = (self.mobs[a].info[4] / self.player.info[3])*self.mobs[a].info[3]
                    if self.player.info[11] > 0:
                        damageTaken = (100-self.player.info[11])/100 * damageTaken
                    self.player.info[4] -= damageTaken
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
        #run spawnercode
        for y in range(len(self.gameMap[0])):
            for x in range(len(self.gameMap)):
                if isinstance(self.gameMap[x][y].gameObject, Spawner):
                    self.gameMap[x][y].gameObject.run(self.gameMap,self.mobs,self.player)

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

        #
        if isinstance(gameObject, LevelEnd):
            #print("Level done!")
            self.levelID += 1
            if self.levelID >= self.levels:
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

    #loads the current level
    def loadLevel(self, levelToLoad = None):
        #if(EndGame):
        #    self.gameWon = True
        #    return
        #if(not levelToLoad is None): # if a levelToLoad is hand over load this level
        self.levelID = levelToLoad
        print("now playing:", self.levelID)
        #else: # else load the level with the next id
        #    self.levelID = self.levelID + 1

        self.gameMap, self.mobs, self.player.info[0], self.player.info[1] = MapHandler.loadMap(self.levelID)
        self.mapHandler.createBorders(self.gameMap, len(self.gameMap),len(self.gameMap[0]))
        self.pathfinding = astar.pathfinder(astar.gamemapNeighbors(self.gameMap))
        self.displayFirst = True