from tkinter import *
from tkinter.filedialog import *
from src.logic.main.Map import *
from src.logic.objects.Monsters import *
import src.logic.objects.Monsters as MonstersModule
import src.logic.objects.GameObjects as GameObjectsModule
import threading
import os
import sys, inspect
'''
A tkinter gui to create maps for the game.
The programm exports to a simple .py file so every export can be edited afterwards by hand.
To create a new Level simply call Levelbuilder() with the wanted width and height.
>>> Levelbuilder(10,20)
'''
def get_default_parameter(func):
    """
    returns a dictionary of arg_name:default_values for the input function
    """
    try:
        parameter, varparameter, keywords, defaults = inspect.getargspec(func)
        return dict(zip(parameter[-len(defaults):], defaults))
    except TypeError as tp:
        return {}


class Levelbuilder():
    def __init__(self,width, height):
        self.possibleGameObjects = ["Empty"] + [i[0] for i in inspect.getmembers(GameObjectsModule, inspect.isclass)]# A list of all possible GameObjects)
        excludes = ["GameObject","Interactable","Item","LevelEnd"]
        self.possibleGameObjects = [x for x in self.possibleGameObjects if x not in excludes]
        self.possibleMobs = ["None"] + [i[0] for i in inspect.getmembers(MonstersModule, inspect.isclass)] # A list of all possible Mobs
        self.possibleMobs = [x for x in self.possibleMobs if x not in excludes]
        self.playerposition =(0,0)
        self.GameObjects =[]
        self.Mobs = []
        self.window = Tk()
        self.window.title('Levelbuilder')
        self.window.minsize(600,400)
        self.window.maxsize(1280,720)
        #PrepareMap
        self.map = Frame(self.window)
        self.map.grid(row=0, column=0)
        self.gameMap = MapHandler().createMap(width,height)

        self.buttonMap = [[None for _ in range(width)] for _ in range(height)]
        xCo = 0
        yCo = 0
        for x in self.gameMap:
            yCo = 0
            for y in x:
                f = Frame(self.map, height=32, width=32)
                f.pack_propagate(0) # don't shrink
                f.grid(row=yCo, column=xCo)
                self.buttonMap[xCo][yCo] = Button(f, command = self.getSettingsFunction(xCo,yCo), height=2, width = 2)
                self.buttonMap[xCo][yCo].bind('<Button-3>', lambda event,xVal=xCo, yVal=yCo: self.setWall(xVal,yVal))
                self.buttonMap[xCo][yCo].bind('<Button-2>', lambda event,xVal=xCo, yVal=yCo: self.setPlayer(xVal,yVal))
                self.buttonMap[xCo][yCo].pack(fill=BOTH, expand=1)
                yCo = yCo + 1
            xCo = xCo + 1
        #select what to show
        self.displayMode=0
        self.updateMap()
        #PrepareSettings
        self.settings = Frame(self.window)
        self.settings.grid(row=0, column=1, sticky=E)
        #Menubar
        self.menubar = Menu(self.window)
        self.menubar.add_command(label="save", command=self.save)
        self.menubar.add_command(label="quit", command=self.window.quit)
        self.menubar.add_command(label="gameobjects", command= lambda : self.setDisplayMode(0))
        self.menubar.add_command(label="mobs", command= lambda : self.setDisplayMode(1))
        self.window.config(menu=self.menubar)
        self.window.mainloop()

    def setWall(self, xCo, yCo):
        self.gameMap[xCo][yCo].isSolid = not self.gameMap[xCo][yCo].isSolid
        self.updateMap()

    def setDisplayMode(self, mode):
        self.displayMode = mode
        self.updateMap()

    def setPlayer(self, xCo, yCo):
        self.playerposition = (xCo,yCo)
        self.updateMap()
    #returns a function oppening the settings for the desired coordinates
    def getSettingsFunction(self,xCo, yCo):
        def function():
            self.openSettings(xCo,yCo)
        return function

    def openSettings(self, x, y):
        self.settings.destroy()
        self.settings = Frame(self.window)
        self.settings.grid(row=0, column=1, sticky=E)
        if(self.displayMode == 0):
            def okButtonFunction():
                self.settings.selectedObject[0] = self.settings.name.get()
                if(not self.settings.selected):
                    return
                self.settings.selectedObject[3] = [cuco.get() for cuco in self.settings.cuCoInput]
                self.setGameObjectAt(x,y, self.settings.selectedObject[0], self.settings.selectedObject[3])
                self.updateMap()
            def selectButtonFunction(event):
                if(self.settings.name.get()== "Empty"):
                    self.deletGameObjectAt(x,y)
                    self.updateMap()
                    self.openSettings(x,y)
                    return
                self.settings.selected = True
                #CustomCOde
                def addCuCoInput():
                    self.settings.cuCoInput.append( Entry(self.settings.CuCoInput))
                    self.settings.cuCoInput[-1].grid(row=len(self.settings.cuCoInput)+1,columnspan=3)
                def removeCuCoInput():
                    self.settings.cuCoInput[-1].destroy()
                    del self.settings.cuCoInput[-1]
                self.settings.cuCoInput = []
                addCuCoInput()
                self.settings.cuCoInputHeader= Label(self.settings.CuCoInput,text='CustomCode')
                self.settings.cuCoInputHeader.grid(row=0,column = 0)
                self.settings.addCuCoButton = Button(self.settings.CuCoInput, text="+", command=addCuCoInput)
                self.settings.addCuCoButton.grid(row=0,column=1)
                self.settings.removeCuCoButton = Button(self.settings.CuCoInput, text="-", command=removeCuCoInput)
                self.settings.removeCuCoButton.grid(row=0,column=2)
                for cuco in self.settings.selectedObject[3]:
                    self.settings.cuCoInput[-1].insert(0, cuco)
                    if(cuco != self.settings.selectedObject[3][-1]):
                        addCuCoInput()

            self.settings.selected = False
            self.settings.ParameterInput = Frame(self.settings)
            self.settings.ParameterInput.grid(row = 2)
            self.settings.CuCoInput = Frame(self.settings)
            self.settings.CuCoInput.grid(row = 2,column=1)
            self.settings.selectedObject = self.getGameObjectAt(x,y)
            if(self.settings.selectedObject is None):
                self.settings.selectedObject = ["Empty",x,y,[]]
                self.settings.containing = False
            else:
                self.settings.containing = True
            self.settings.name = StringVar()
            self.settings.name.set(self.settings.selectedObject[0])
            self.settings.description = Label(self.settings,text='Choose an Object')
            self.settings.description.grid(row=0)
            self.settings.dropdown_Object = OptionMenu(self.settings, self.settings.name,*self.possibleGameObjects,command=selectButtonFunction)
            self.settings.dropdown_Object.grid(row=1, column=0)
            self.settings.okButton = Button(self.settings, text="save", command=okButtonFunction)
            self.settings.okButton.grid(sticky=SW)
            if(self.settings.containing is True):
                selectButtonFunction()
        else: #mob settings
            def okButtonFunction():

                if(not self.settings.selected):
                    return
                self.settings.selectedMob[4] = [cuco.get() for cuco in self.settings.cuCoInput]
                self.settings.selectedMob[3] = [","+ self.settings.parameterLabels[a].cget("text")+"="+ self.settings.parameterInputFields[a].get() for a in range(len(self.settings.parameterLabels))]
                self.setMobAt(x,y, self.settings.selectedMob[0], self.settings.selectedMob[3],self.settings.selectedMob[4])
                self.updateMap()
            def selectButtonFunction(event):
                if(self.settings.name.get()== "None"):
                    self.deleteMobAt(x,y)
                    self.updateMap()
                    self.openSettings(x,y)
                    return
                self.settings.selected = True
                self.settings.selectedMob[0] = self.settings.name.get()
                self.settings.parameterLabels = []
                self.settings.parameterInputFields = []
                defaults = get_default_parameter(eval(self.settings.selectedMob[0]))
                if(not defaults == {}): #if there are no defaultarguments return and do not offer this menu
                    for key in defaults:
                        self.settings.parameterLabels.append(Label(self.settings.ParameterInput,text=key))
                        self.settings.parameterLabels[-1].grid(row= len(self.settings.parameterLabels), column = 0)
                        self.settings.parameterInputFields.append(Entry(self.settings.ParameterInput))
                        self.settings.parameterInputFields[-1].insert(0,defaults.get(key, None))
                        self.settings.parameterInputFields[-1].grid(row= len(self.settings.parameterInputFields), column = 1)
                        print(key)
                    #HeaderArguments
                    self.settings.parameterInputHeader= Label(self.settings.ParameterInput,text='Arguments')
                    self.settings.parameterInputHeader.grid(row=0,column = 0)
                #CustomCode
                def addCuCoInput():
                    self.settings.cuCoInput.append( Entry(self.settings.CuCoInput))
                    self.settings.cuCoInput[-1].grid(row=len(self.settings.cuCoInput)+1,columnspan=3)
                def removeCuCoInput():
                    self.settings.cuCoInput[-1].destroy()
                    del self.settings.cuCoInput[-1]
                self.settings.cuCoInput = []
                addCuCoInput()
                #HeaderArguments
                self.settings.cuCoInputHeader= Label(self.settings.CuCoInput,text='CustomCode')
                self.settings.cuCoInputHeader.grid(row=0,column = 0)
                self.settings.addCuCoButton = Button(self.settings.CuCoInput, text="+", command=addCuCoInput)
                self.settings.addCuCoButton.grid(row=0,column=1)
                self.settings.removeCuCoButton = Button(self.settings.CuCoInput, text="-", command=removeCuCoInput)
                self.settings.removeCuCoButton.grid(row=0,column=2)
                for cuco in self.settings.selectedMob[4]:
                    self.settings.cuCoInput[-1].insert(0, cuco)
                    if(cuco != self.settings.selectedMob[4][-1]):
                        addCuCoInput()
            self.settings.selected = False
            self.settings.ParameterInput = Frame(self.settings)
            self.settings.ParameterInput.grid(row = 2)
            self.settings.CuCoInput = Frame(self.settings)
            self.settings.CuCoInput.grid(row = 2,column=1)
            self.settings.selectedMob = self.getMobAt(x,y)
            if(self.settings.selectedMob is None):
                self.settings.selectedMob = ["None",x,y,{},[]]
                self.settings.containing = False
            else:
                self.settings.containing = True
            self.settings.name = StringVar()
            self.settings.name.set(self.settings.selectedMob[0])
            self.settings.description = Label(self.settings,text='Choose an Mob')
            self.settings.description.grid(row=0)
            self.settings.dropdown_Object = OptionMenu(self.settings, self.settings.name,*self.possibleMobs,command=selectButtonFunction)
            self.settings.dropdown_Object.grid(row=1, column=0)
            self.settings.okButton = Button(self.settings, text="save", command=okButtonFunction)
            self.settings.okButton.grid(sticky=SW)
            if(self.settings.containing is True):
                selectButtonFunction()

    def updateMap(self):
        #clears the map
        for x in self.buttonMap:
            for y in x:
                y.config(text="")
        #displays solid tiles as black and nosolid as white
        for x in range(len(self.buttonMap)):
            for y in range(len(self.buttonMap[0])):
                if( self.gameMap[x][y].isSolid is True):
                    self.buttonMap[x][y].config(bg="black")
                    self.buttonMap[x][y].config(fg="white")
                else:
                    self.buttonMap[x][y].config(bg="white")
                    self.buttonMap[x][y].config(fg="Black")

        #shows the playerposition
        self.buttonMap[self.playerposition[0]][self.playerposition[1]].config(text="P")

        if self.displayMode == 0:
            for gO in self.GameObjects:
                try:
                    self.buttonMap[gO[1]][gO[2]].image = PhotoImage(file="../../resources/" + gO[0]+"default.png")
                    self.buttonMap[gO[1]][gO[2]].config(image=self.buttonMap[gO[1]][gO[2]].image)
                except Exception:
                    self.buttonMap[gO[1]][gO[2]].config(text=gO[0][0])
        else:
            for mob in self.Mobs:
                try:
                    self.buttonMap[mob[1]][mob[2]].image = PhotoImage(file="../../resources/" + mob[0]+".png")
                    self.buttonMap[mob[1]][mob[2]].config(image=self.buttonMap[mob[1]][mob[2]].image)
                except Exception:
                    self.buttonMap[mob[1]][mob[2]].config(text=mob[0][0])
    '''
    saves the edited map to the selected file by replacing [WallDeclarations], [ObjectDeclarations] and [MobDeclarations]
    '''
    def save(self):
        path = asksaveasfilename() #asks for a filepath
        print(path)
        #prepares Tiles
        resultMap = ""
        xCo = 0
        yCo = 0
        for x in self.gameMap:
            for y in x:
                if( self.gameMap[xCo][yCo].getIsSolid is True):
                    resultMap += "gameMap[" + str(xCo) + "]["+str(yCo)+"] = Wall()\n"
                else:
                    resultMap += "gameMap[" + str(xCo) + "]["+str(yCo)+"] = Ground()\n"
                yCo = yCo + 1
            yCo = 0
            xCo = xCo + 1

        #prepares items and other gameobjects
        resultObjects =  ""
        for gO in self.GameObjects:
            resultObjects += "gameMap["+str(gO[1])+"]["+str(gO[2])+"].setGameObject("+str(gO[0])+"())\n"
            if not (gO[3] is None):
                for CustomCode in gO[3]:
                    resultObjects +="gameMap["+str(gO[1])+"]["+str(gO[2])+"].gameObject."+str(CustomCode)+"\n"
        #prepares Mobs
        resultMobs = ""
        for mob in self.Mobs:
            resultMobs += "mobs.append("+str(mob[0])+"("+str(mob[1])+", "+str(mob[2])+"".join(mob[3])+"))\n"
            if not (mob[4] is []):
                for CustomCode in mob[4]:
                    resultMobs += "mobs[-1]."+str(CustomCode)+"\n"

        template = open('././resources/maps/levelTemplate.py', 'r').read() #opens the templete file
        updatedFile = template.split("[WallDeclarations]")[0]+ resultMap.replace("\n", "\n    ") + template.split("[WallDeclarations]")[1]
        updatedFile = updatedFile.split("[ObjectDeclarations]")[0]+ resultObjects.replace("\n", "\n    ") + updatedFile.split("[ObjectDeclarations]")[1]
        updatedFile = updatedFile.split("[MobDeclarations]")[0] + resultMobs.replace("\n", "\n    ") + updatedFile.split("[MobDeclarations]")[1]
        updatedFile = updatedFile.replace("<playerPositionX>", str(self.playerposition[0]))
        updatedFile = updatedFile.replace("<playerPositionY>", str(self.playerposition[1]))
        open(path,"w").write(updatedFile) #writes the edited file to filesystem


    #================Functions for editing mobs and gameobjects at specific places===========
    def getGameObjectAt(self, x,y):
        for gO in self.GameObjects:
            if(gO[1]== x and gO[2]== y):
                return gO
        return None

    def setGameObjectAt(self, x, y, name, customCodes):
        self.GameObjects.append([name,x,y,customCodes])
        self.updateMap()

    def deletGameObjectAt(self,x,y):
        for gameobject in self.GameObjects:
            if(gameobject[1]== x and gameobject[2]== y):
                self.GameObjects.remove(gameobject)

    def getMobAt(self, x,y):
        for mob in self.Mobs:
            if(mob[1]== x and mob[2]== y):
                return mob
        return None

    def setMobAt(self, x, y, name, parameter, customCodes):
        if(name == "None"):
           self.deleteMobAt(x,y)
           return
        self.Mobs.append([name,x,y,parameter, customCodes])
        self.updateMap()

    def deleteMobAt(self,x,y):
         for mob in self.Mobs:
            if(mob[1]== x and mob[2]== y):
                self.Mobs.remove(mob)

#level = Levelbuilder(20,10)#starts a Levelbuilder