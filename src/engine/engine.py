import json
#pseudocode
class Engine():
    def __init__(self):
        self.outputFile ="pyUnity.json"
        self.open()
    def render(self, tiles, playerInfo, mobs):
        print("render")
        mapTiles = tiles
        overlayTiles = tiles
        #prepare MapS
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
        #prepareOverlay
        xCo = 0
        yCo = 0
        for _ in overlayTiles:
            for tile in _:
                    overlayTiles[xCo][yCo] = tile.item.ID
                yCo = yCo + 1
            xCo = xCo + 1
        #write File
        file = open(self.outputFile, "w")
        #TODO: Remove the indent for builds
        x = json.dumps({"tiles": tiles, "overlay": overlayTiles, "playerStats": playerInfo, "mobs": mobs },indent=4)
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
        engineReady = False
        while not engineReady:
            engine = open("unityPy.txt", "r")
            x = engine.readline()
            print(x)
            engineReady = (x == "ready") # pseudo code
