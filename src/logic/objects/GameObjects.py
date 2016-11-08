from src.logic.main.Item import *
from src.logic.objects.Monsters import Hunter
from random import randint

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
'''
Spawners
'''
#spawns weak funters with great range to prevent the player form getting overpowered
class HunterSpawner(Spawner):
    def __init__(self, delay=5, initDelay=False,spawnPoints=[(1,1),(2,2)]):
        Spawner.__init__(self, delay=delay ,initDelay=False)
        self.spawnPoints = spawnPoints
    def _spawn(self, gameMap, mobs, player):
        entry = randint(0,len(self.spawnPoints))
        mobs.append(Hunter(self.spawnPoints[entry][0],0,2,10,50))