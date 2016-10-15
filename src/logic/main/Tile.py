from src.logic.main.Item import NoItem
#TODO: clean this up, getters and setters 
#Tile superclass contains needed variables and methods for all tiles
class Tile(object):
    def __init__(self, isSolid, item):
        self.isSolid = isSolid
        self.item = item

    def setItem(self, item):
        self.item = item
    
    def getIsSolid(self):
        return self.isSolid
        
class Ground(Tile):
    def __init__(self, item):
        Tile.__init__(self, False, item)
        
    #only used for "text"-engine no need to keep it afterwards
    def getTile(self):
        return "Ground"
    
class Wall(Tile):
    def __init__(self):
        Tile.__init__(self, True, NoItem())
    
    #only used for "text"-engine no need to keep it afterwards
    def getTile(self):
        return "Wall"