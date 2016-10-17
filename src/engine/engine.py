import json
#pseudocode
class Engine():
    def __init__(self):
        self.outputFile = "pyUnity.json" #TODO: redirect to temp folder
        self.open()

    def display(self, tiles, playerInfo, mobs):
        print("render")
        mapTiles = tiles
        overlayTiles = tiles
        #prepare map
        xCo = 0
        yCo = 0
        for _ in mapTiles:
            for tile in _:
                if( tile.getIsSolid() is False ): # pseudocode
                    mapTiles[xCo][yCo] = 1 # wall
                else:
                    mapTiles[xCo][yCo] = 0 # ground
                yCo = yCo + 1
            xCo = xCo + 1
        #prepare overlay
        xCo = 0
        yCo = 0
        for _ in overlayTiles:
            for tile in _:
                overlayTiles[xCo][yCo] = tile.item.ID
                yCo = yCo + 1
            xCo = xCo + 1
        #prepare mobs
        mobsInfos = []
        for mob in mobs:
            mobsInfos.append(mob.info)
        #write File
        file = open(self.outputFile, "w")
        #TODO: Remove the indent for builds
        x = json.dumps({"tiles": tiles, "overlay": overlayTiles, "playerInfo": playerInfo, "mobsInfos": mobsInfos },indent=4)
        file.write(x)
        file.close()

    def close(self):
        file = open(self.outputFile, "w")
        file.write("close")
        file.close()

    def open(self):
        file = open(self.outputFile, "w")
        file.write("loading")
        file.close()
        #TODO run build of unityGame
        engineReady = False
        while not engineReady:
            engine = open("unityPy.txt", "r") #TODO: redirect to temp folder
            x = engine.readline()
            print(x)
            engineReady = (x == "ready") # pseudo code
