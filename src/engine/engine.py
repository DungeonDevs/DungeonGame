#pseudocode
class engine():
    def __init__(self):
        self.outputFile ="pyUnity.txt"
        self.open=""
    def render(self, data):
        file = open(self.outputFile, "w")
        #TODO output data
    def close(self):
        file = open(self.outputFile, "w")
        file.write("close")
    def open(self):
        file = open(self.outputFile, "w")
        file.write("loading")
        engineReady = False
        while not engineReady:
            engine = open("unityPy.txt", "r")
            engineReady = engine.readline == "ready" # pseudo code
