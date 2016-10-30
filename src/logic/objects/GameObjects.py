from src.logic.main.Item import *

'''
CollectableItems
'''
#first real item, increases attack by 10
class Sword(Item):
    def __init__(self):
        Item.__init__(self, 12, 0, False, healthUp=0, attackUp=10)
'''
class RedSwordOfFire(Item):
    def __init__(self):
        Item.__init__(self, 13, 0, False, 1, 16)
class BlueSwordOfRain(Item):
    def __init__(self):
        Item.__init__(self, 14, 0, False, 3, 13)
class BlackSwordOfDeath(Item):
    def __init__(self):
        Item.__init__(self, 15, 0, False, 0, 25)
class WhiteSwordOfIllumination(Item):
    def __init__(self):
        Item.__init__(self, 16, 0, False, 10, 20)
class MysticalStickOfMagicAndFantasy(Item):
    def __init__(self):
        Item.__init__(self, 19, 0, False, 0, 0)
class Stick(Item):
    def __init__(self):
        Item.__init__(self, 110, 0, False, 0, 2)
#increases defence by 2
class FeatherChestplate(Item):
    def __init__(self):
        Item.__init__(self, 111, 0, False, 1, 0)
'''
'''
InteractableGameObjects
'''
class ItemAppears(Interactable):
    def __init__(self, positionX=0, positionY=0, item=Empty()):
        Interactable.__init__(self, 21, 0, False)
        self.positionX = positionX
        self.positionY = positionY
        self.item = item
    def interact(self, player, gameMap, mobs):
        gameMap[self.positionX][self.positionY].setGameObject(self.item)