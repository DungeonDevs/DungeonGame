from tkinter import *
from src.logic.main.Map import *
import os

class Levelbuilder():
    def __init__(self, width, height):
        self.window = Tk()
        self.window.title('Levelbuilder')
        self.window.minsize(600,400)
        self.window.maxsize(1280,720)
        self.map = Frame(self.window)
        self.map.grid(row=0, column=0)
        self.settings = Frame(self.window)
        self.settings.grid(row=0, column=1)
        self.gameMap = MapHandler().createMap(width,height)
        self.buttonMap = [[None for _ in range(width)] for _ in range(height)]
        xCo = 0
        yCo = 0
        for x in self.gameMap:
            for y in x:
                self.buttonMap[xCo][yCo] = Button(self.map, command = self.getFunction(xCo,yCo))
                self.buttonMap[xCo][yCo].grid(row=yCo, column=xCo)
                yCo = yCo + 1
            yCo = 0
            xCo = xCo + 1
        self.updateMap()
        e1 = Entry(self.settings)
        e2 = Entry(self.settings)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        self.window.mainloop()

    def getFunction(self,xCo, YCo):
        def function():
            self.openSettings(xCo,YCo)
        return function

    def openSettings(self, x, y):
        self.updateMap()

    def updateMap(self):
        xCo = 0
        yCo = 0
        for x in self.buttonMap:
            for y in x:
                if( self.gameMap[xCo][yCo].getIsSolid is True):
                    self.buttonMap[xCo][yCo].config(bg="black")
                else:
                    self.buttonMap[xCo][yCo].config(bg="white")
                if(not isinstance( self.gameMap[xCo][yCo].gameObject, Empty)):
                    self.buttonMap[xCo][yCo].config(text="X")
                else:
                    self.buttonMap[xCo][yCo].config(text="O")
                yCo = yCo + 1
            yCo = 0
            xCo = xCo + 1

        def save(self, path):
            resultMap = ""
            xCo = 0
            yCo = 0
            for x in self.gameMap:
                for y in x:
                    if( self.gameMap[xCo][yCo].getIsSolid is True):
                        resultMap.add("gameMap[" + xCo + "]["+yCo+"] = Wall()\n")
                    else:
                        resultMap.add("gameMap[" + xCo + "]["+yCo+"] = Ground()\n")
                    yCo = yCo + 1
                yCo = 0
                xCo = xCo + 1

            #Items and other Gameobjects
            resultObjects = ""
            for gO in self.Objects:
                if(go[3] is None): # if there are no special arguments
                    resultObjects.add("gameMap[{gO[1]}][{gO[2]}].setGameObject({go[0]}())\n")
                else:
                     resultObjects.add("gameMap[{gO[1]}][{gO[2]}].setGameObject({go[0]}(*{go[3]}))\n")
                if not (go[4] is None):
                    for CustomCode in go[4]:
                        resultObjects.add("gameMap[{gO[1]}][{gO[2]}].gameObject.{CustomCode}\n")
            string = string.replace("\n", "\n    ")
            #mobs
            resultMobs = ""
            for mob in self.mobs:
                if(mob[1] is None): # if there are no special arguments
                    resultMobs.add("mobs.append({go[0]}())\n")
                else:
                    resultMobs.add("mobs.append({go[0]}(*{go[1]}))\n")
                if not (go[2] is None):
                    for CustomCode in go[2]:
                        resultMobs.add("mobs[-1].{CustomCode}\n")
            #readfile
            #file = readfile()
            updatedFile = file.split("[WallDeclarations]")[0]+ resultMap + file.split("[WallDeclarations]")[1]
            updatedFile = updateFile.split("[ObjectDeclarations]")[0]+ resultObjects + updateFile.split("[ObjectDeclarations]")[1]
            updatedFile = updateFile.split("[MobDeclarations]")[0]+ resultObjects + updateFile.split("[MobDeclarations]")[1]
            #format somehow
            #string = string.replace("\n", "\n    ") #intend
            #writefile
level = Levelbuilder(10,10)