#superclass contains shared variables
class Item():
    def __init__(self, ID, orientation, isSolid, healthUp, attackUp):
        self.ID = ID
        self.orientation = orientation
        self.isSolid = isSolid
        self.healthUp = healthUp
        self.attackUp = attackUp

#used to indicate that there is no item
class NoItem(Item):
    def __init__(self):
        Item.__init__(self, 0, 0, False, 0, 0)

#test item to see if solid works        
class SolidItem(Item):
    def __init__(self):
        Item.__init__(self, 1, 0, True, 0, 0)

#first real item, increases attack by 10        
class Sword(Item):
    def __init__(self):
        Item.__init__(self, 2, 0, False, 0, 10)