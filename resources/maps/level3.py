from src.logic.main.Map import *
from src.logic.objects.GameObjects import *
from src.logic.objects.Monsters import *
def getLevel():
    size = [20,20]
    mapHandler = MapHandler()
    gameMap = mapHandler.createMap(*size)

    gameMap[0][0] = Wall()
    gameMap[0][1] = Wall()
    gameMap[0][2] = Wall()
    gameMap[0][3] = Wall()
    gameMap[0][4] = Wall()
    gameMap[0][5] = Wall()
    gameMap[0][6] = Wall()
    gameMap[0][7] = Wall()
    gameMap[0][8] = Wall()
    gameMap[0][9] = Wall()
    gameMap[0][10] = Wall()
    gameMap[0][11] = Wall()
    gameMap[0][12] = Wall()
    gameMap[0][13] = Wall()
    gameMap[0][14] = Wall()
    gameMap[0][15] = Wall()
    gameMap[0][16] = Wall()
    gameMap[0][17] = Wall()
    gameMap[0][18] = Wall()
    gameMap[0][19] = Wall()
    gameMap[1][0] = Wall()
    gameMap[1][1] = Ground(Empty())
    gameMap[1][2] = Ground(Empty())
    gameMap[1][3] = Ground(Empty())
    gameMap[1][4] = Wall()
    gameMap[1][5] = Ground(Empty())
    gameMap[1][6] = Ground(Empty())
    gameMap[1][7] = Ground(Empty())
    gameMap[1][8] = Ground(Empty())
    gameMap[1][9] = Wall()
    gameMap[1][10] = Wall()
    gameMap[1][11] = Ground(Empty())
    gameMap[1][12] = Wall()
    gameMap[1][13] = Ground(Empty())
    gameMap[1][14] = Ground(Empty())
    gameMap[1][15] = Ground(Empty())
    gameMap[1][16] = Ground(Empty())
    gameMap[1][17] = Wall()
    gameMap[1][18] = Ground(Empty())
    gameMap[1][19] = Wall()
    gameMap[2][0] = Wall()
    gameMap[2][1] = Ground(Empty())
    gameMap[2][2] = Ground(Empty())
    gameMap[2][3] = Ground(Empty())
    gameMap[2][4] = Wall()
    gameMap[2][5] = Wall()
    gameMap[2][6] = Ground(Empty())
    gameMap[2][7] = Wall()
    gameMap[2][8] = Ground(Empty())
    gameMap[2][9] = Ground(Empty())
    gameMap[2][10] = Ground(Empty())
    gameMap[2][11] = Ground(Empty())
    gameMap[2][12] = Wall()
    gameMap[2][13] = Ground(Empty())
    gameMap[2][14] = Wall()
    gameMap[2][15] = Ground(Empty())
    gameMap[2][16] = Wall()
    gameMap[2][17] = Ground(Empty())
    gameMap[2][18] = Ground(Empty())
    gameMap[2][19] = Wall()
    gameMap[3][0] = Wall()
    gameMap[3][1] = Ground(Empty())
    gameMap[3][2] = Ground(Empty())
    gameMap[3][3] = Ground(Empty())
    gameMap[3][4] = Wall()
    gameMap[3][5] = Ground(Empty())
    gameMap[3][6] = Ground(Empty())
    gameMap[3][7] = Wall()
    gameMap[3][8] = Ground(Empty())
    gameMap[3][9] = Wall()
    gameMap[3][10] = Wall()
    gameMap[3][11] = Wall()
    gameMap[3][12] = Wall()
    gameMap[3][13] = Ground(Empty())
    gameMap[3][14] = Ground(Empty())
    gameMap[3][15] = Ground(Empty())
    gameMap[3][16] = Ground(Empty())
    gameMap[3][17] = Wall()
    gameMap[3][18] = Ground(Empty())
    gameMap[3][19] = Wall()
    gameMap[4][0] = Wall()
    gameMap[4][1] = Wall()
    gameMap[4][2] = Ground(Empty())
    gameMap[4][3] = Wall()
    gameMap[4][4] = Wall()
    gameMap[4][5] = Ground(Empty())
    gameMap[4][6] = Wall()
    gameMap[4][7] = Ground(Empty())
    gameMap[4][8] = Ground(Empty())
    gameMap[4][9] = Wall()
    gameMap[4][10] = Ground(Empty())
    gameMap[4][11] = Ground(Empty())
    gameMap[4][12] = Ground(Empty())
    gameMap[4][13] = Ground(Empty())
    gameMap[4][14] = Wall()
    gameMap[4][15] = Wall()
    gameMap[4][16] = Ground(Empty())
    gameMap[4][17] = Ground(Empty())
    gameMap[4][18] = Ground(Empty())
    gameMap[4][19] = Wall()
    gameMap[5][0] = Wall()
    gameMap[5][1] = Wall()
    gameMap[5][2] = Ground(Empty())
    gameMap[5][3] = Wall()
    gameMap[5][4] = Wall()
    gameMap[5][5] = Ground(Empty())
    gameMap[5][6] = Wall()
    gameMap[5][7] = Wall()
    gameMap[5][8] = Wall()
    gameMap[5][9] = Wall()
    gameMap[5][10] = Ground(Empty())
    gameMap[5][11] = Wall()
    gameMap[5][12] = Wall()
    gameMap[5][13] = Wall()
    gameMap[5][14] = Ground(Empty())
    gameMap[5][15] = Ground(Empty())
    gameMap[5][16] = Ground(Empty())
    gameMap[5][17] = Wall()
    gameMap[5][18] = Ground(Empty())
    gameMap[5][19] = Wall()
    gameMap[6][0] = Wall()
    gameMap[6][1] = Wall()
    gameMap[6][2] = Ground(Empty())
    gameMap[6][3] = Ground(Empty())
    gameMap[6][4] = Ground(Empty())
    gameMap[6][5] = Ground(Empty())
    gameMap[6][6] = Wall()
    gameMap[6][7] = Ground(Empty())
    gameMap[6][8] = Ground(Empty())
    gameMap[6][9] = Ground(Empty())
    gameMap[6][10] = Ground(Empty())
    gameMap[6][11] = Wall()
    gameMap[6][12] = Wall()
    gameMap[6][13] = Ground(Empty())
    gameMap[6][14] = Ground(Empty())
    gameMap[6][15] = Wall()
    gameMap[6][16] = Ground(Empty())
    gameMap[6][17] = Wall()
    gameMap[6][18] = Ground(Empty())
    gameMap[6][19] = Wall()
    gameMap[7][0] = Wall()
    gameMap[7][1] = Ground(Empty())
    gameMap[7][2] = Ground(Empty())
    gameMap[7][3] = Wall()
    gameMap[7][4] = Wall()
    gameMap[7][5] = Wall()
    gameMap[7][6] = Wall()
    gameMap[7][7] = Ground(Empty())
    gameMap[7][8] = Wall()
    gameMap[7][9] = Wall()
    gameMap[7][10] = Wall()
    gameMap[7][11] = Ground(Empty())
    gameMap[7][12] = Ground(Empty())
    gameMap[7][13] = Ground(Empty())
    gameMap[7][14] = Wall()
    gameMap[7][15] = Ground(Empty())
    gameMap[7][16] = Ground(Empty())
    gameMap[7][17] = Wall()
    gameMap[7][18] = Wall()
    gameMap[7][19] = Wall()
    gameMap[8][0] = Wall()
    gameMap[8][1] = Wall()
    gameMap[8][2] = Ground(Empty())
    gameMap[8][3] = Ground(Empty())
    gameMap[8][4] = Ground(Empty())
    gameMap[8][5] = Ground(Empty())
    gameMap[8][6] = Ground(Empty())
    gameMap[8][7] = Ground(Empty())
    gameMap[8][8] = Ground(Empty())
    gameMap[8][9] = Ground(Empty())
    gameMap[8][10] = Ground(Empty())
    gameMap[8][11] = Ground(Empty())
    gameMap[8][12] = Ground(Empty())
    gameMap[8][13] = Wall()
    gameMap[8][14] = Wall()
    gameMap[8][15] = Wall()
    gameMap[8][16] = Ground(Empty())
    gameMap[8][17] = Wall()
    gameMap[8][18] = Ground(Empty())
    gameMap[8][19] = Wall()
    gameMap[9][0] = Wall()
    gameMap[9][1] = Wall()
    gameMap[9][2] = Ground(Empty())
    gameMap[9][3] = Wall()
    gameMap[9][4] = Wall()
    gameMap[9][5] = Ground(Empty())
    gameMap[9][6] = Wall()
    gameMap[9][7] = Ground(Empty())
    gameMap[9][8] = Wall()
    gameMap[9][9] = Wall()
    gameMap[9][10] = Ground(Empty())
    gameMap[9][11] = Ground(Empty())
    gameMap[9][12] = Wall()
    gameMap[9][13] = Ground(Empty())
    gameMap[9][14] = Ground(Empty())
    gameMap[9][15] = Ground(Empty())
    gameMap[9][16] = Ground(Empty())
    gameMap[9][17] = Ground(Empty())
    gameMap[9][18] = Ground(Empty())
    gameMap[9][19] = Wall()
    gameMap[10][0] = Wall()
    gameMap[10][1] = Wall()
    gameMap[10][2] = Ground(Empty())
    gameMap[10][3] = Ground(Empty())
    gameMap[10][4] = Wall()
    gameMap[10][5] = Ground(Empty())
    gameMap[10][6] = Wall()
    gameMap[10][7] = Ground(Empty())
    gameMap[10][8] = Ground(Empty())
    gameMap[10][9] = Ground(Empty())
    gameMap[10][10] = Wall()
    gameMap[10][11] = Ground(Empty())
    gameMap[10][12] = Wall()
    gameMap[10][13] = Ground(Empty())
    gameMap[10][14] = Wall()
    gameMap[10][15] = Ground(Empty())
    gameMap[10][16] = Wall()
    gameMap[10][17] = Wall()
    gameMap[10][18] = Ground(Empty())
    gameMap[10][19] = Wall()
    gameMap[11][0] = Wall()
    gameMap[11][1] = Wall()
    gameMap[11][2] = Wall()
    gameMap[11][3] = Wall()
    gameMap[11][4] = Wall()
    gameMap[11][5] = Ground(Empty())
    gameMap[11][6] = Wall()
    gameMap[11][7] = Ground(Empty())
    gameMap[11][8] = Wall()
    gameMap[11][9] = Wall()
    gameMap[11][10] = Wall()
    gameMap[11][11] = Ground(Empty())
    gameMap[11][12] = Wall()
    gameMap[11][13] = Ground(Empty())
    gameMap[11][14] = Wall()
    gameMap[11][15] = Ground(Empty())
    gameMap[11][16] = Ground(Empty())
    gameMap[11][17] = Ground(Empty())
    gameMap[11][18] = Wall()
    gameMap[11][19] = Wall()
    gameMap[12][0] = Wall()
    gameMap[12][1] = Ground(Empty())
    gameMap[12][2] = Ground(Empty())
    gameMap[12][3] = Ground(Empty())
    gameMap[12][4] = Ground(Empty())
    gameMap[12][5] = Ground(Empty())
    gameMap[12][6] = Wall()
    gameMap[12][7] = Ground(Empty())
    gameMap[12][8] = Ground(Empty())
    gameMap[12][9] = Ground(Empty())
    gameMap[12][10] = Wall()
    gameMap[12][11] = Ground(Empty())
    gameMap[12][12] = Ground(Empty())
    gameMap[12][13] = Ground(Empty())
    gameMap[12][14] = Wall()
    gameMap[12][15] = Ground(Empty())
    gameMap[12][16] = Wall()
    gameMap[12][17] = Ground(Empty())
    gameMap[12][18] = Wall()
    gameMap[12][19] = Wall()
    gameMap[13][0] = Wall()
    gameMap[13][1] = Ground(Empty())
    gameMap[13][2] = Wall()
    gameMap[13][3] = Ground(Empty())
    gameMap[13][4] = Wall()
    gameMap[13][5] = Ground(Empty())
    gameMap[13][6] = Wall()
    gameMap[13][7] = Ground(Empty())
    gameMap[13][8] = Wall()
    gameMap[13][9] = Ground(Empty())
    gameMap[13][10] = Wall()
    gameMap[13][11] = Ground(Empty())
    gameMap[13][12] = Wall()
    gameMap[13][13] = Ground(Empty())
    gameMap[13][14] = Ground(Empty())
    gameMap[13][15] = Ground(Empty())
    gameMap[13][16] = Wall()
    gameMap[13][17] = Ground(Empty())
    gameMap[13][18] = Wall()
    gameMap[13][19] = Wall()
    gameMap[14][0] = Wall()
    gameMap[14][1] = Wall()
    gameMap[14][2] = Ground(Empty())
    gameMap[14][3] = Ground(Empty())
    gameMap[14][4] = Wall()
    gameMap[14][5] = Ground(Empty())
    gameMap[14][6] = Ground(Empty())
    gameMap[14][7] = Ground(Empty())
    gameMap[14][8] = Wall()
    gameMap[14][9] = Wall()
    gameMap[14][10] = Wall()
    gameMap[14][11] = Wall()
    gameMap[14][12] = Wall()
    gameMap[14][13] = Wall()
    gameMap[14][14] = Wall()
    gameMap[14][15] = Ground(Empty())
    gameMap[14][16] = Wall()
    gameMap[14][17] = Ground(Empty())
    gameMap[14][18] = Wall()
    gameMap[14][19] = Wall()
    gameMap[15][0] = Wall()
    gameMap[15][1] = Ground(Empty())
    gameMap[15][2] = Wall()
    gameMap[15][3] = Wall()
    gameMap[15][4] = Ground(Empty())
    gameMap[15][5] = Ground(Empty())
    gameMap[15][6] = Wall()
    gameMap[15][7] = Ground(Empty())
    gameMap[15][8] = Ground(Empty())
    gameMap[15][9] = Ground(Empty())
    gameMap[15][10] = Ground(Empty())
    gameMap[15][11] = Ground(Empty())
    gameMap[15][12] = Wall()
    gameMap[15][13] = Ground(Empty())
    gameMap[15][14] = Ground(Empty())
    gameMap[15][15] = Ground(Empty())
    gameMap[15][16] = Wall()
    gameMap[15][17] = Ground(Empty())
    gameMap[15][18] = Wall()
    gameMap[15][19] = Wall()
    gameMap[16][0] = Wall()
    gameMap[16][1] = Ground(Empty())
    gameMap[16][2] = Ground(Empty())
    gameMap[16][3] = Wall()
    gameMap[16][4] = Ground(Empty())
    gameMap[16][5] = Wall()
    gameMap[16][6] = Wall()
    gameMap[16][7] = Wall()
    gameMap[16][8] = Wall()
    gameMap[16][9] = Ground(Empty())
    gameMap[16][10] = Wall()
    gameMap[16][11] = Ground(Empty())
    gameMap[16][12] = Wall()
    gameMap[16][13] = Ground(Empty())
    gameMap[16][14] = Wall()
    gameMap[16][15] = Wall()
    gameMap[16][16] = Ground(Empty())
    gameMap[16][17] = Ground(Empty())
    gameMap[16][18] = Ground(Empty())
    gameMap[16][19] = Wall()
    gameMap[17][0] = Wall()
    gameMap[17][1] = Wall()
    gameMap[17][2] = Ground(Empty())
    gameMap[17][3] = Ground(Empty())
    gameMap[17][4] = Ground(Empty())
    gameMap[17][5] = Wall()
    gameMap[17][6] = Ground(Empty())
    gameMap[17][7] = Ground(Empty())
    gameMap[17][8] = Ground(Empty())
    gameMap[17][9] = Ground(Empty())
    gameMap[17][10] = Wall()
    gameMap[17][11] = Ground(Empty())
    gameMap[17][12] = Wall()
    gameMap[17][13] = Ground(Empty())
    gameMap[17][14] = Ground(Empty())
    gameMap[17][15] = Ground(Empty())
    gameMap[17][16] = Ground(Empty())
    gameMap[17][17] = Ground(Empty())
    gameMap[17][18] = Ground(Empty())
    gameMap[17][19] = Wall()
    gameMap[18][0] = Wall()
    gameMap[18][1] = Ground(Empty())
    gameMap[18][2] = Ground(Empty())
    gameMap[18][3] = Wall()
    gameMap[18][4] = Ground(Empty())
    gameMap[18][5] = Ground(Empty())
    gameMap[18][6] = Ground(Empty())
    gameMap[18][7] = Wall()
    gameMap[18][8] = Wall()
    gameMap[18][9] = Ground(Empty())
    gameMap[18][10] = Ground(Empty())
    gameMap[18][11] = Ground(Empty())
    gameMap[18][12] = Ground(Empty())
    gameMap[18][13] = Ground(Empty())
    gameMap[18][14] = Ground(Empty())
    gameMap[18][15] = Wall()
    gameMap[18][16] = Ground(Empty())
    gameMap[18][17] = Ground(Empty())
    gameMap[18][18] = Ground(Empty())
    gameMap[18][19] = Wall()
    gameMap[19][0] = Wall()
    gameMap[19][1] = Wall()
    gameMap[19][2] = Wall()
    gameMap[19][3] = Wall()
    gameMap[19][4] = Wall()
    gameMap[19][5] = Wall()
    gameMap[19][6] = Wall()
    gameMap[19][7] = Wall()
    gameMap[19][8] = Wall()
    gameMap[19][9] = Wall()
    gameMap[19][10] = Wall()
    gameMap[19][11] = Wall()
    gameMap[19][12] = Wall()
    gameMap[19][13] = Wall()
    gameMap[19][14] = Wall()
    gameMap[19][15] = Wall()
    gameMap[19][16] = Wall()
    gameMap[19][17] = Wall()
    gameMap[19][18] = Wall()
    gameMap[19][19] = Wall()


    # ObjectDeclarations is replaced with declarations following the style:  gameMap[<X>][<Y>].setGameObject(<ObjectName>()).
    # in edge cases you can add special Arguments gameMap[<X>][<Y>].setGameObject(<ObjectName>(*<Arguments>))
    # or add custom code gameMap[<X>][<Y>].gameObject.<CustomCode>
    gameMap[3][1].setGameObject(Sword())
    gameMap[3][3].setGameObject(Sword())
    gameMap[17][17].setGameObject(LevelEnd(ID=999,isSolid=0))

    mobs = []
    # MobDeclarations is replaced with declarations following the style:  mobs.append(<Mobname>()).
    # in edge cases you can add special Arguments mobs.append(<Mobname>(*<Arguments>))
    # or add custom code mobs[-1].<CustomCode>
    mobs.append(Slime(7, 2,orientation=0))
    mobs.append(Hunter(6, 4,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(3, 6,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(13, 9,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(8, 11,attack=20,orientation=0,health=10,eyesight=5))
    mobs.append(Slime(9, 11,orientation=0))
    mobs.append(Hunter(8, 10,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(14, 17,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(17, 15,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(17, 11,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Slime(5, 16,orientation=0))
    mobs.append(Hunter(3, 15,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(5, 10,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(17, 2,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(12, 4,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(10, 5,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(17, 9,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(8, 7,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(12, 7,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(13, 1,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(17, 8,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(18, 13,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(13, 14,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(11, 13,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(7, 16,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(4, 13,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(2, 10,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(8, 3,attack=2,orientation=0,health=10,eyesight=5))
    mobs.append(Hunter(6, 2,attack=2,orientation=0,health=10,eyesight=5))


    playerPositionX = 2
    playerPositionY = 2
    return gameMap, mobs, playerPositionX, playerPositionY