from src.logic.tiles import Tiles
class Printer(object):
    info = {Tiles.Ground : 0, Tiles.Wall : 1}
    def display(self, gameMap):
        for y in range(len(gameMap)):
            row = ''
            for x in range(len(gameMap[0])):
                row += str(Printer.info[gameMap[x][y]])
            print(row)    