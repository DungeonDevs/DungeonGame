from src.logic.main.Map import *
from src.logic.objects.GameObjects import *
from src.logic.objects.Monsters import *
def getLevel():
    size = [6,6]
    mapHandler = MapHandler()
    gameMap = mapHandler.createMap(*size)

    gameMap[0][0] = Wall()
    gameMap[0][1] = Wall()
    gameMap[0][2] = Wall()
    gameMap[0][3] = Wall()
    gameMap[0][4] = Wall()
    gameMap[0][5] = Wall()
    gameMap[1][0] = Wall()
    gameMap[1][1] = Ground(Empty())
    gameMap[1][2] = Ground(Empty())
    gameMap[1][3] = Wall()
    gameMap[1][4] = Ground(Empty())
    gameMap[1][5] = Wall()
    gameMap[2][0] = Wall()
    gameMap[2][1] = Wall()
    gameMap[2][2] = Ground(Empty())
    gameMap[2][3] = Ground(Empty())
    gameMap[2][4] = Ground(Empty())
    gameMap[2][5] = Wall()
    gameMap[3][0] = Wall()
    gameMap[3][1] = Ground(Empty())
    gameMap[3][2] = Ground(Empty())
    gameMap[3][3] = Wall()
    gameMap[3][4] = Ground(Empty())
    gameMap[3][5] = Wall()
    gameMap[4][0] = Wall()
    gameMap[4][1] = Wall()
    gameMap[4][2] = Ground(Empty())
    gameMap[4][3] = Ground(Empty())
    gameMap[4][4] = Wall()
    gameMap[4][5] = Wall()
    gameMap[5][0] = Wall()
    gameMap[5][1] = Wall()
    gameMap[5][2] = Wall()
    gameMap[5][3] = Wall()
    gameMap[5][4] = Wall()
    gameMap[5][5] = Wall()


    # ObjectDeclarations is replaced with declarations following the style:  gameMap[<X>][<Y>].setGameObject(<ObjectName>()).
    # in edge cases you can add special Arguments gameMap[<X>][<Y>].setGameObject(<ObjectName>(*<Arguments>))
    # or add custom code gameMap[<X>][<Y>].gameObject.<CustomCode>
    gameMap[4][3].setGameObject(LevelEnd(ID=999,isSolid=0))

    mobs = []
    # MobDeclarations is replaced with declarations following the style:  mobs.append(<Mobname>()).
    # in edge cases you can add special Arguments mobs.append(<Mobname>(*<Arguments>))
    # or add custom code mobs[-1].<CustomCode>
    mobs.append(Hunter(3, 4,attack=2,eyesight=5,orientation=0,health=10))
    mobs.append(Hunter(1, 4,attack=2,eyesight=5,orientation=0,health=10))
    mobs.append(Hunter(3, 1,attack=2,eyesight=5,orientation=0,health=10))
    mobs.append(Hunter(1, 1,attack=2,eyesight=5,orientation=0,health=10))
    mobs.append(Hunter(4, 2,attack=2,eyesight=5,orientation=0,health=10))
    mobs.append(Hunter(3, 2,attack=2,eyesight=5,orientation=0,health=10))


    playerPositionX = 2
    playerPositionY = 2
    return gameMap, mobs, playerPositionX, playerPositionY