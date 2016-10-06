import json
#pseudocode
class engine():
    def __init__(self):
        self.outputFile ="pyUnity.json"
        self.open=""
    def render(self, tiles, overlay = None, Held= None):
        file = open(self.outputFile, "w")
        x = json.dumps({'tiles': tiles, 'overlay': overlay, 'player': {"roataion": None, "stats": {}}},indent=4)
        file.write(x)
        #TODO output data
        file.close()
    def close(self):
        file = open(self.outputFile, "w")
        file.write("close")
        file.close()
    def open(self):
        file = open(self.outputFile, "w")
        file.write("loading\n")
        file.close()
        engineReady = False
        while not engineReady:
            engine = open("unityPy.txt", "r")
            engineReady = engine.readline == "ready" # pseudo code
