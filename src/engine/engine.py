import json
#pseudocode
class engine():
    def __init__(self):
        self.outputFile ="pyUnity.json"
        self.open()
    def render(self, tiles, overlay = None, rotation = 0):
        print("render")
        file = open(self.outputFile, "w")
        x = json.dumps({"tiles": tiles, "overlay": overlay, "playerRoataion": rotation, "playerStats": None},indent=4)
        file.write(x)
        #TODO output data
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
