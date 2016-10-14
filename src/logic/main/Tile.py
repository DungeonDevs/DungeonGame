class Tile(object):
    def __init__(self, isSolid):
        self.isSolid = isSolid
        
class Ground(Tile):
    def __init__(self, item):
        Tile.__init__(self, False)
        self.item = item

    def setItem(self, item):
        self.item = item
        
    def getTile(self):
        return "Ground"
    
class Wall(Tile):
    def __init__(self):
        Tile.__init__(self, True)
    
    def getTile(self):
        return "Wall"