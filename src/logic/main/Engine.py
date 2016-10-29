#everything is temporary and is in no way optimized
class Engine(object):
    info ={"Ground": 0, "Wall": 1}
    def __init__(self):
        pass
    def display(self, gameMap, playerInfo, mobs):
        field = ["" for x in range(len(gameMap[0]))]
        row = ""
        for y in range(len(gameMap[0])):
            for x in range(len(gameMap)):
                row += str(self.info[gameMap[x][y].getTile()])
                if gameMap[x][y].gameObject.ID != 0:
                    row += str(gameMap[x][y].gameObject.ID)
                else:
                    row += " "
            field[y] = row
            row = ""

        replace = field[playerInfo[1]]
        replace = replace[0: 2 * playerInfo[0]] + "P " + replace[2 * (playerInfo[0] + 1): -1] + " "
        field[playerInfo[1]] = replace

        for a in range(len(mobs)):
            replace = field[mobs[a].info[1]]
            replace = replace[0: 2 * mobs[a].info[0]] + "M " + replace[2 * (mobs[a].info[0] + 1): -1] + " "
            field[mobs[a].info[1]] = replace

        for y in range(len(gameMap[0])):
            print(field[y])
        #print("Health: " + str(playerInfo[4])+ "/" + str(playerInfo[5].stats[2]) + " Attack: " + str(playerInfo[3]) + " Healing: " + str(playerInfo[5].stats[3]))
        print(playerInfo[0:5] + playerInfo[6:12])

class InputHandler(object):
    def getInput(self):
        return input("Move:")