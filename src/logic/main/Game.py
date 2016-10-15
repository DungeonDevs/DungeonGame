from src.logic.main.Map import MapHandler
from src.logic.main.Entity import Player, Monster

from src.logic.main.Engine import Engine, InputHandler
from src.logic.main.Item import NoItem, Sword
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
    #gameMap[2][2] = Wall()
    #gameMap[2][4].setItem(SolidItem())
    player = Player(1,1,1,10,30, None)
    mobs = [Monster(5,5,0,5,21),Monster(5,5,0,5,21),Monster(5,5,0,5,21)]
    #mobs += [Monster(5,5,0,5,21)]
    #mobs += [Monster(4,4,0,5,21)]
    #mobs += [Monster(2,6,0,5,21)]
    running = True
        
    def __init__(self):
        self.mapHandler.createBorders(self.gameMap, 10,10)
        while self.running:
            self.tick()
            
    def tick(self):
        self.display()
        self.playerMove()
        self.mobMove()
        self.fight()
        self.itemAction()
                   
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
                if self.player.info[4] <= 0:
                    print("You lost!")
                    self.running = False
                else:
                    dead += [a]
        
        for a in range(len(dead)):
            self.mobs.pop(dead[a])
            
    def itemAction(self):
        if self.gameMap[self.player.info[0]][self.player.info[1]].item != NoItem():
            self.player.info[3] += self.gameMap[self.player.info[0]][self.player.info[1]].item.attackUp
            self.player.info[4] += self.gameMap[self.player.info[0]][self.player.info[1]].item.healthUp
            self.gameMap[self.player.info[0]][self.player.info[1]].setItem(NoItem())