class Tile(object):
    def __init__(self, isSolid):
        self.isSolid = isSolid
        
class Ground(Tile):
    Tile.__init__(isSolid = False)

class Wall(Tile):
    Tile.__init__(isSolid = True)