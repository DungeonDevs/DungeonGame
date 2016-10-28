from src.logic.main.Item import Empty

#Tile superclass contains needed variables and methods for all tiles
class Tile(object):
    def __init__(self, isSolid, gameObject):
        self.isSolid = isSolid
        self.gameObject = gameObject

    def setGameObject(self, gameObject):
        self.gameObject = gameObject

    def getIsSolid(self):
        return self.isSolid

class Ground(Tile):
    def __init__(self, gameObject):
        Tile.__init__(self, False, gameObject)

    #only used for "text"-engine no need to keep it afterwards
    def getTile(self):
        return "Ground"

class Wall(Tile):
    def __init__(self):
        Tile.__init__(self, True, Empty())

    #only used for "text"-engine no need to keep it afterwards
    def getTile(self):
        return "Wall"