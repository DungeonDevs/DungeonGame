'''
superclasses
'''
class GameObject():
    def __init__(self, ID, orientation, isSolid):
        self.ID = ID
        self.orientation = orientation
        self.isSolid = isSolid

#superclass contains shared variables
#ID starts with 1
class Item(GameObject):
    def __init__(self, ID, orientation, isSolid, healthUp=0, attackUp=0, healingUp=0, intelligenceUp=0, intuitionUp=0, dexterityUp=0, agilityUp=0, blockUp=0):
        GameObject.__init__(self, ID, orientation, isSolid)
        self.healthUp = healthUp
        self.attackUp = attackUp
        self.healingUp = healingUp
        self.intelligenceUp = intelligenceUp
        self.intuitionUp = intuitionUp
        self.dexterityUp = dexterityUp
        self.agilityUp = agilityUp
        self.blockUp = blockUp
#superclass for all objects that shall interact with the gameMap, the monbs or the player itself and not just with the player stats
#ID starts with 2
class Interactable(GameObject):
    def __init__(self, ID, orientation, isSolid):
        GameObject.__init__(self, ID, orientation, isSolid)
    def interact(self, player, gameMap, mobs):
        print("Interaction triggered! Override for use!")

#superclass for all objects that shall end a level (or call another level)
#ID starts with 3
class LevelEnd(GameObject) :
    def __init__(self, ID = 999, isSolid = False):
        GameObject.__init__(self, ID, 0, False)

    #call the callback with a specific levelId
    #def trigger(self, callback):
    #    print("LevelEnd triggered! Override for use!")

'''
MetaItems
'''
#used to indicate that there is no item
class Empty(GameObject):
    def __init__(self):
        GameObject.__init__(self, 0, 0, False)

#test item to see if solid works
class SolidItem(Item):
    def __init__(self):
        Item.__init__(self, 11, 0, True, 0, 0)