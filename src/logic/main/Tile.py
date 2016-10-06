class Tile(object):
    def __init__(self, item, isSolid):
        self.item = item
        self.isSolid = isSolid
        
class Ground(Tile):
    pass

class Wall(Tile):
    pass