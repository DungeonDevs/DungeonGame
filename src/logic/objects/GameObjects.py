from src.logic.main.Item import GameObject, Item, Interactable, LevelEnd
#TODO: Split this file into multiple files (Items, Interactables, Levelchanges etc.)
'''
CollectableItems
'''
#first real item, increases attack by 10
class Sword(Item):
    def __init__(self):
        Item.__init__(self, 12, 0, False, 0, 10)
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
InteractableGameObjects
'''
class Leather(Interactable):
    def __init__(self):
        Interactable.__init__(self, 21, 0, False)
    def interact(self, player, gameMap, mobs):
        gameMap[4][4].setGameObject(Sword())