from src.logic.main.Map import *
from src.logic.objects.GameObjects import *
from src.logic.objects.Monsters import *
def getLevel():
    size = [10,10]
    mapHandler = MapHandler()
    gameMap = mapHandler.createMap(*size)

    # [ObjectDeclarations] is replaced with declarations following the style:  gameMap[<X>][<Y>].setGameObject(<ObjectName>()).
    # in edge cases you can add special Arguments gameMap[<X>][<Y>].setGameObject(<ObjectName>(*<Arguments>))
    # or add custom code gameMap[<X>][<Y>].gameObject.<CustomCode>

    #[ObjectDeclarations]
    gameMap[5][5].setGameObject(Sword())
    mobs = []
    # [MobDeclarations] is replaced with declarations following the style:  mobs.append(<Mobname>()).
    # in edge cases you can add special Arguments mobs.append(<Mobname>(*<Arguments>))
    # or add custom code mobs[1].<CustomCode>

    #[MobDeclarations]
    mobs.append(Hunter(5,6,0))

    playerPositionX = 2
    playerPositionY = 1
    return gameMap, mobs, playerPositionX, playerPositionY