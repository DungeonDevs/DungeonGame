from src.logic.main.Map import *
from src.logic.objects import GameObjects, Monsters
def getLevel():
    size = [<width>,<height>]
    mapHandler = MapHandler()
    gameMap = mapHandler.createMap(*size)

    [WallDeclarations]

    # [ObjectDeclarations] is replaced with declarations following the style:  gameMap[<X>][<Y>].setGameObject(<ObjectName>()).
    # in edge cases you can add special Arguments gameMap[<X>][<Y>].setGameObject(<ObjectName>(*<Arguments>))
    # or add custom code gameMap[<X>][<Y>].gameObject.<CustomCode>
    [ObjectDeclarations]
    mobs = []
    # [MobDeclarations] is replaced with declarations following the style:  mobs.append(<Mobname>()).
    # in edge cases you can add special Arguments mobs.append(<Mobname>(*<Arguments>))
    # or add custom code mobs[-1].<CustomCode>
    [MobDeclarations]

    playerPositionX = <playerPositionX>
    playerPositionY = <playerPositionY>
    return gameMap, mobs, playerPositionX, playerPositionY