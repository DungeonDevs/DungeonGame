from src.logic.main.Map import *
from src.logic.objects.GameObjects import *
from src.logic.objects.Monsters import *
def getLevel():
    size = [7,5]
    mapHandler = MapHandler()
    gameMap = mapHandler.createMap(*size)

    gameMap[0][0] = Ground(Empty())
    gameMap[0][1] = Ground(Empty())
    gameMap[0][2] = Ground(Empty())
    gameMap[0][3] = Ground(Empty())
    gameMap[0][4] = Ground(Empty())
    gameMap[0][5] = Ground(Empty())
    gameMap[0][6] = Ground(Empty())
    gameMap[1][0] = Ground(Empty())
    gameMap[1][1] = Wall()
    gameMap[1][2] = Wall()
    gameMap[1][3] = Wall()
    gameMap[1][4] = Ground(Empty())
    gameMap[1][5] = Ground(Empty())
    gameMap[1][6] = Ground(Empty())
    gameMap[2][0] = Ground(Empty())
    gameMap[2][1] = Ground(Empty())
    gameMap[2][2] = Ground(Empty())
    gameMap[2][3] = Ground(Empty())
    gameMap[2][4] = Wall()
    gameMap[2][5] = Ground(Empty())
    gameMap[2][6] = Ground(Empty())
    gameMap[3][0] = Ground(Empty())
    gameMap[3][1] = Ground(Empty())
    gameMap[3][2] = Ground(Empty())
    gameMap[3][3] = Ground(Empty())
    gameMap[3][4] = Ground(Empty())
    gameMap[3][5] = Wall()
    gameMap[3][6] = Ground(Empty())
    gameMap[4][0] = Ground(Empty())
    gameMap[4][1] = Ground(Empty())
    gameMap[4][2] = Ground(Empty())
    gameMap[4][3] = Ground(Empty())
    gameMap[4][4] = Ground(Empty())
    gameMap[4][5] = Ground(Empty())
    gameMap[4][6] = Ground(Empty())
    

    # ObjectDeclarations is replaced with declarations following the style:  gameMap[<X>][<Y>].setGameObject(<ObjectName>()).
    # in edge cases you can add special Arguments gameMap[<X>][<Y>].setGameObject(<ObjectName>(*<Arguments>))
    # or add custom code gameMap[<X>][<Y>].gameObject.<CustomCode>
    gameMap[3][3].setGameObject(Sword())
    
    mobs = []
    # MobDeclarations is replaced with declarations following the style:  mobs.append(<Mobname>()).
    # in edge cases you can add special Arguments mobs.append(<Mobname>(*<Arguments>))
    # or add custom code mobs[-1].<CustomCode>
    

    playerPositionX = 2
    playerPositionY = 1
    return gameMap, mobs, playerPositionX, playerPositionY