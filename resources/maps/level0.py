from src.logic.main.Map import *
from src.logic.objects.GameObjects import *
from src.logic.objects.Monsters import *
def getLevel():
    size = [10,15]
    mapHandler = MapHandler()
    gameMap = mapHandler.createMap(*size)

    # [ObjectDeclarations] is replaced with declarations following the style:  gameMap[<X>][<Y>].setGameObject(<ObjectName>()).
    # in edge cases you can add special Arguments gameMap[<X>][<Y>].setGameObject(<ObjectName>(*<Arguments>))
    # or add custom code gameMap[<X>][<Y>].gameObject.<CustomCode>

    #[ObjectDeclarations]
    gameMap[5][5].setGameObject(LevelEnd())
    gameMap[6][7].setGameObject(ItemAppears(positionX=2,positionY=2,item=Sword()))
    mobs = []
    # [MobDeclarations] is replaced with declarations following the style:  mobs.append(<Mobname>()).
    # in edge cases you can add special Arguments mobs.append(<Mobname>(*<Arguments>))
    # or add custom code mobs[1].<CustomCode>

    #[MobDeclarations]
    mobs.append(Hunter(5,6,0))
    mobs.append(Hunter(4,6,0))
    mobs.append(Hunter(3,6,0))
    mobs.append(Hunter(2,6,0))
    mobs.append(Hunter(4,4,0))
    mobs.append(Hunter(6,5,0))

    playerPositionX = 2
    playerPositionY = 1
    return gameMap, mobs, playerPositionX, playerPositionY