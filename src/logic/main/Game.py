from src.logic.main.Map import MapHandler
from src.logic.main.Entity import Player

from src.logic.main.Engine import Engine, InputHandler
class Game(object):
    
    engine = Engine()
    inputHandler = InputHandler()
    mapHandler = MapHandler()
    gameMap = mapHandler.createMap(10, 10)
    #gameMap[5][5].setItem(1)
    player = Player(1,1,0,1,1, None)
    running = True
        
    def __init__(self):
        while self.running:
            self.tick()
            
    def tick(self):
        self.engine.display(self.gameMap, self.player.xPos, self.player.yPos, self.player.orientation)
        
        inputKey = self.inputHandler.getInput()
        if inputKey == "w":
            self.player.move()
        elif inputKey == "a":
            self.player.orientation -= 1
            if self.player.orientation < 0:
                self.player.orientation = 3
        elif inputKey == "d":
            self.player.orientation += 1
            if self.player.orientation > 3:
                self.player.orientation = 0
        elif inputKey == "stop":
            self.running = False
            
        