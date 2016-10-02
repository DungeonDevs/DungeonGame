from src.logic.tiles import Tiles

class Map(object):
    def __init__(self, width, height):
        self.gameMap = [[Tiles.Ground for x in range(width)] for y in range(height)]
