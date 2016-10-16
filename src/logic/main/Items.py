from src.logic.main.Item import Item, Interactable, LevelEnd, GameObject
'''
CollectableItems
'''
#first real item, increases attack by 10
class Sword(Item):
    def __init__(self):
        Item.__init__(self, 2, 0, False, 0, 10)
'''
InteractableItems
'''
class Leather(Interactable):
    def __init__(self):
        Interactable.__init__(self, 3, 0, False)
    def interact(self, player, gameMap, mobs):
        gameMap[4][4].setGameObject(Sword())