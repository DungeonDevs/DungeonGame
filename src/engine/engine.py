import json
#pseudocode
class Engine():
    def __init__(self):
        self.outputFile ="pyUnity.json"
        self.open()
    def render(self, tiles, dictionary = None, rotation = 0):
        print("render")
        mapTiles = tiles
        overlayTiles = tiles
        xCo = 0
        yCo = 0
        for _ in mapTiles:
            for tile in _:
                if( tile.begehbar is False ): # pseudocode
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
                if( tile.item == None ): # pseudocode
                    overlayTiles[xCo][yCo] = 0
                else:
                    overlayTiles[xCo][yCo] = dictionary.get(tile.item) # pseudocode
                yCo = yCo + 1
            xCo = xCo + 1

        file = open(self.outputFile, "w")
        x = json.dumps({"tiles": tiles, "overlay": overlayTiles, "playerRoataion": rotation, "playerStats": None},indent=4)
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
